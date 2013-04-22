#-*- coding:utf-8 -*-
'''
Created on 2013-4-17

@author: cheng
'''
from django.contrib.auth import authenticate
from Login.models import Account
from MemManage.models import TempRole,Role,HeadPhoto
from django.utils.translation import ugettext as _

def fetcheVerifyInfo(params):
    '''
    fetch verify info of given temprole code
    
    @param code: invite code
    '''
    result=dict()
    #dafault none verify
    result["verifyByName"]="false"
    result["verifyByIdcard"]="false"
    result["verifyByQuest"]="false"
    result["verifyQuest"]=""
    
    code=params["code"]
    tempRole=TempRole.objects.get(code=code)
    if tempRole.verifyByName==1:
        #verify by name activated
        result["verifyByName"]="true"
    if tempRole.verifyByIdCard==1:
        result["verifyByIdcard"]="true"
    if tempRole.verifyByQuest==1:
        result["verifyByQuest"]="true"
        result["verifyQuest"]=tempRole.verifyQuest
    
    return result
    
def verify(params,tempRole):
    '''
    verify role to permit
    '''
    errors=[]
    flag=True
    if "verifyName" in params and tempRole.name<>params["verifyName"]:
        singleError=dict()
        singleError["eid"]="21041"
        singleError["msg"]=_("验证姓名不一致")
        errors.append(singleError)
        flag=False
    if "verifyIdcard" in params and tempRole.idcard<>params["verifyIdcard"]:
        singleError=dict()
        singleError["eid"]="21051"
        singleError["msg"]=_("验证身份证号不一致")
        errors.append(singleError)
        flag=False
    if "verifyAnswer" in params and tempRole.verifyAnswer<>params["verifyAnswer"]:
        singleError=dict()
        singleError["eid"]="21121"
        singleError["msg"]=_("验证自定义问题答案不一致")
        errors.append(singleError)
        flag=False
    return flag,errors

def confirmRole(params):
    '''
    confirm role info and to normal page
    @param create: whether create or login of account
    @param aname: account name
    @param apass: account password
    @param code: invite code
    
    Optional:
    @param verifyName: name to be verified
    @param verifyIdcard: idcard to be verified
    @param verifyAnswer: answer to be verified
    '''
    result=dict()
    code=params["code"]
    tempRole=TempRole.objects.get(code=code)
    if params["create"]=="false":       
        aname=params["aname"]
        apass=params["apass"]        
        #authentication
        account=authenticate(username=aname,password=apass)
        if account is None:
            accountNone=dict()
            accountNone["eid"]="20001"
            accountNone["msg"]=_("账户登陆错误")
            result["success"]="false"
            result["errors"]=accountNone
            return result
    else:
        flag,errors=verify(params,tempRole)
        if flag:
            if len(Account.objects.filter(aname=params["aname"]))>0:
                result["success"]="false"
                accountDupError=dict()
                accountDupError["eid"]="21012"
                accountDupError["msg"]=_("帐号名已被注册")
                result["errors"]=accountDupError
                return result     
            account=Account.objects.create_user(username=params["aname"], password=params["apass"])
        else:
            result["success"]="false"
            result["errors"]=errors
            return result
    #insert info to Role from TempRole and delete TempRole info
    
    role=Role()
        
    role.name=tempRole.name
    role.idcard=tempRole.idcard
    role.sex=-1         #default unknow
    role.phone=tempRole.phone
    role.email=tempRole.email
    role.permission=tempRole.permission
    role.company=tempRole.company
    role.account=account
    role.location="Unknown"     #unknow?
    role.head_photo=HeadPhoto.objects.get(hid=1)    #default
        
    try:
        role.save()
        tempRole.delete()
            
        #delete session of code
        result["success"]="true"
        result["rid"]=role.rid
        result["cid"]=role.company_id
        result["rlevel"]=role.permission
    except:
        result["success"]="false"
        result["errors"]=""        
    print result    
    return result
