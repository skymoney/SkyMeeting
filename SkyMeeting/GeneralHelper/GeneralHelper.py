#-*-coding:utf-8 -*-
'''
Created on 2013-4-17

@author: cheng
'''
from Meeting.models import *
from MemManage.models import *

def getDashboard(account):
    '''
    get all info given one specified account
    @param account: account obj
    '''
    #corresponding roles of account,at least one
    dashInfoSet=[]
    
    role_set=account.role_set.all()
    for role in role_set:
        dashInfoSingle=dict()
        dashInfoSingle["rid"]=role.rid
        dashInfoSingle["cid"]=role.company_id
        dashInfoSingle["companyName"]=role.company.cname
        dashInfoSingle["companyAdmin"]=role.company.role_set.filter(account_id=1)[0].name
        dashInfoSingle["membersCount"]=len(role.company.role_set.all())
        meeting_set=Meeting.objects.filter(meeting_participant__role_id=role.rid)
        active_set=meeting_set.filter(meeting_status__lt=10)
        dashInfoSingle["allMeetingsCount"]=len(meeting_set)
        dashInfoSingle["activeMeetingsCount"]=len(active_set)
        dashInfoSingle["closedMeetingsCount"]=len(meeting_set.filter(meeting_status=15))
        latestMeeting=dict()
        if len(active_set)>0:            
            lastMeeting=active_set.order_by("start_time")[0]
            latestMeeting["mtitle"]=lastMeeting.meeting_title
            latestMeeting["mstart"]=lastMeeting.start_time.strftime("%Y/%m/%d %H:%M")
            latestMeeting["mplace"]=lastMeeting.meeting_place
        dashInfoSingle["latestMeeting"]=latestMeeting
        dashInfoSet.append(dashInfoSingle)
    
    return dashInfoSet

def getProfile(params):
    '''
    get personal profile given specified id
    @param rid: role id
    '''    
    role=Role.objects.get(rid=params["rid"])
    profileInfo=dict()
    profileInfo["name"]=role.name
    profileInfo["sex"]=role.sex
    profileInfo["idcard"]=role.idcard
    profileInfo["phone"]=role.phone
    profileInfo["email"]=role.email
    
    return profileInfo

def editProfile(params):
    '''
    edit profile and save info
    @param rid: id of role to edited
    @param name: name of role
    @param sex: sex of role
    @param idcard: idcard of role
    @param phone: phone number of role
    @param email: email of role
    '''
    result=dict()
    
    role=Role.objects.get(rid=params["rid"])
    role.name=params["name"]
    role.sex=int(params["sex"])
    role.idcard=params["idcard"]
    role.phone=params["phone"]
    role.email=params["email"]
    
    try:
        role.save()
        result["success"]="true"
    except:
        result["success"]="false"
        result["errors"]=""
    return result

def changePwdViaEmail(params):
    '''
    user change pwd via email
    @param email: email to be sended 
    '''
    from hashlib import md5
    from django.conf import settings
    email=params["email"]
    result=dict()
    flag,rid=checkEmail(email)
    if flag:
        #add more ops here
        newParams=dict()
        newParams["email"]=email
        newParams["rid"]=rid
        return changePwdSendEmail(newParams)
    else:
        result["success"]="false"
        result["errors"]="Email Does Not Exist"
        return result

def changePwdSendEmail(params):
    '''
    change password via admin
    @param email: email of target user
    @param rid: role id of target user
    '''
    from django.core.mail import send_mail
    from django.conf import settings
    from hashlib import md5
    from datetime import datetime
    from Login.models import TempAccountPwd
    result=dict()
    email=params["email"]
    aid=Role.objects.get(rid=params["rid"]).account
    code=md5(email+str(aid.aid)+str(datetime.now())).hexdigest()
    
    tmp=TempAccountPwd()
    tmp.tapAid=aid
    tmp.tapCode=code
    tmp.tapDate=datetime.now()
    
    try:
        tmp.save()
        content="点击以下链接修改您的密码 \n"+"http://192.168.100.21/"      #here needs to be conf to proper url
        resultCode=send_mail("修改您的账户密码",content,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        
        if resultCode==1:
            result["success"]="true"
        else:
            result["success"]="false"
            result["errors"]="send fail"
    except:
        result["success"]="false"
        result["errors"]="save fail"
    return result


def changePwdVerify(params):
    '''
    verify whether has proper code on changing pwd
    @param code: code of changing pwd
    '''
    code=params["code"]
    from Login.models import TempAccountPwd
    tempAccount=TempAccountPwd.objects.filter(tapCode=code)
    result=dict()
    if len(tempAccount)>0:
        result["success"]="true"
        result["aid"]=tempAccount[0].aid
        result["aname"]=tempAccount[0].aname
    else:
        result["success"]="false"
    return result

def changePwdEdit(params):
    '''
    finally edit pwd of target account
    @param pwd: new password to be stored
    @param aid: id of target account
    '''
    from Login.models import Account
    result=dict()
    try:
        Account.objects.filter(aid=params["aid"]).update(apassword=params["pwd"])
        result["success"]="true"
    except:
        result["success"]="false"
        result["errors"]="edit fail"

def checkEmail(email):
    '''
    check email exist in db
    '''
    flag=False
    r_set=Role.objects.filter(email=email)
    if len(r_set)>0:
        flag=True
        rid=r_set[0].rid
    
    #add validation here
    return flag,rid