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

def checkMeetingPermission(role):
    #check permission of creating meeting
    #@param role: role to check
    if role.permission==1:
        return True
    else:
        return False