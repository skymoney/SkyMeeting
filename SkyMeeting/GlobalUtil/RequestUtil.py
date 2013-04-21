#-*- coding:utf-8 -*-
from django.conf import settings

def getLangPack(request):
    langPack = dict()
    langPack["LANGUAGES"] = settings.LANGUAGES
    langPack["curLangCode"] = request.LANGUAGE_CODE
    langPack["curAction"] = request.get_full_path
    
    for lang in settings.LANGUAGES:
        if lang[0] == request.LANGUAGE_CODE:
            langPack["curLangName"]=lang[1]
            break
    
    return langPack

def getRolePack(request):
    roleSet=request.user.role_set.all()
    roleSetInfo=[]
    for role in roleSet:
        singleRole=dict()
        singleRole["rid"]=role.rid
        singleRole["name"]=role.name
        singleRole["cid"]=role.company_id
        singleRole["companyName"]=role.company.cname
        roleSetInfo.append(singleRole)
    
    rolePack = dict()
    rolePack["roles"] = roleSetInfo
    rolePack["curRid"] = request.session["rid"] if "rid" in request.session else request.user.role_set.all()[0].rid
    rolePack["curRid"] = int(rolePack["curRid"])    #request.session["rid"] is a string
    return rolePack

def getAuthPack(request):
    authPack = dict()
    authPack["alevel"] = int(request.user.alevel)
    authPack["rlevel"] = int(request.session["rlevel"])
    return authPack

def checkIsLogin(request):
    #check user whether login
    if request.user.is_authenticated():
        return True
    else:
        return False

def checkManagePermission(request):
    #check permission
    #highest 1
    #then 2 ...
    if checkIsLogin(request) and int(request.user.alevel)==1:
        #highest permission
        return True
    else:
        return False

def checkMeetingPermission(rid):
    #check permission of creating meeting
    #@param rid: role to check
    from MemManage.models import Role
    if Role.objects.get(rid=rid).permission==1:
        return True
    else:
        return False
    
def checkRoleMeetingPermission(params):
    '''
    check permission of specified role to edit specified meeting
    
    @param rid: id of role
    @param mid: id of meeting
    '''
    from Meeting.models import Meeting
    if len(Meeting.objects.filter(meeting_id=params["mid"],create_user_id=params["rid"]))>0:
        return True
    return False

def pagingOps(data,order_by,pn):
    '''
    '''
    result=dict()
    startNumber=(int(pn)-1)*settings.NUMBERPERPAGE
    newData=data.order_by(order_by)[startNumber:startNumber+settings.NUMBERPERPAGE]
    
    result["totalNumber"]=len(data)
    result["newData"]=newData
    
    return result
