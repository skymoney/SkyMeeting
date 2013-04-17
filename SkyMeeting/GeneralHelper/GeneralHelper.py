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
            latestMeeting["mstart"]=lastMeeting.start_time
            latestMeeting["mplace"]=lastMeeting.meeting_place
        dashInfoSingle["latestMeeting"]=latestMeeting
        dashInfoSet.append(dashInfoSingle)
    
    return dashInfoSet

def editCurRid(params):
    pass

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
