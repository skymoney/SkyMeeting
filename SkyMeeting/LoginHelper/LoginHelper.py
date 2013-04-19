#-*- coding:utf-8 -*-
'''
Created on 2013-4-17

@author: cheng
'''
from django.contrib.auth import authenticate
from Login.models import Account
from MemManage.models import TempRole,Role,HeadPhoto

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
    if tempRole.verifyByIdcard==1:
        result["verifyByIdcard"]="true"
    if tempRole.verifyByQuest==1:
        result["verifyByQuest"]="true"
        result["verifyQuest"]=tempRole.verifyQuest
    
    return result
    
def verify(params,tempRole):
    '''
    verify role to permit
    '''
    if "verifyName" in params and tempRole.name<>params["verifyName"]:
        return False
    if "verifyIdcard" in params and tempRole.idcard<>params["verifyIdcard"]:
        return False
    if "verifyAnswer" in params and tempRole.verifyAnswer<>params["verifyAnswer"]:
        return False
    return True

def confirmRole(params):
    '''
    confirm role info and to normal page
    @param create: whether create or login of account
    @param aname: account name
    @param apassword: account password
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
    else:
        if verify(params,tempRole):
            if len(Account.objects.filter(aname=params["aname"]))>0:
                result["success"]="false"
                result["errors"]="already have account name"
                return result     
            account=Account.objects.create_user(username=params["aname"], password=params["apass"])
        else:
            result["success"]="false"
            result["errors"]="verify not passed"
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
    except:
        result["success"]="false"
        result["errors"]=""        
    print result    
    return result
