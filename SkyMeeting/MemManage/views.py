#-*-coding:utf-8-*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from MemManageHelper import DAOHelper
import simplejson as json

def member(request):
    #member ops including visiting
    return render_to_response('members.html',Context(DAOHelper.member(request)))

def editRoleInfo(request):
    #save specified role info
    return HttpResponse(json.dumps(DAOHelper.editRoleInfo(request)))    

def addGroup(request):
    #add new group    
    return HttpResponse(json.dumps(DAOHelper.addGroup(request)))

def addTag(request):
    #add new tag
    return HttpResponse(json.dumps(DAOHelper.addTag(request)))

def inviteUser(request):
    #permission check
    #......
    
    params = dict()
    params["cid"] = 1   #default!!!
    params["name"] = request.POST["name"]                           #string
    params["idcard"] = request.POST["idcard"]                       #string
    params["phone"] = request.POST["phone"]                         #string
    params["email"] = request.POST["email"]                         #string
    params["verifyMode"] = request.POST["verifyMode"]               # "1": by name; "2": by idcard; "9": by question
                                                                    # "1+2": by name and idcard;  etc.
                                                                    #  "": without verification
    params["verifyQuestion"] = request.POST["verifyQuestion"]       #string
    params["verifyAnswer"] = request.POST["verifyAnswer"]           #string
    
    #hard code!!!
    result = dict()
    result["success"] = "true"
#    exception
#    result["success"] = "false"
#    result["errors"] = ""
    
    return HttpResponse(json.dumps(result))
    