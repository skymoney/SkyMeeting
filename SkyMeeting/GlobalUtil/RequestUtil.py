#-*- coding:utf-8 -*-
from django.conf import settings

def getLangPack(request):
    langPack = dict()
    langPack["LANGUAGES"] = settings.LANGUAGES
    langPack["curLangCode"] = request.LANGUAGE_CODE
    langPack["curAction"] = request.path
    
    for lang in settings.LANGUAGES:
        if lang[0] == request.LANGUAGE_CODE:
            langPack["curLangName"]=lang[1]
            break
    
    return langPack