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
    #permission check
    #......
    params = dict()
    params["id"] = request.POST["id"]                               #edit user id
    params["name"] = request.POST["name"]
    params["sex"] = request.POST["sex"]
    params["idcard"] = request.POST["idcard"]
    params["phone"] = request.POST["phone"]
    params["email"] = request.POST["email"]
    params["groupIds"] = request.POST["groupIds"]                   # "" for no groups selected, or "1+2" etc.
    params["tagIds"] = request.POST["tagIds"]                       # "" for no tags selected, or "1+2+3" etc.
    
    #save specified role info
    return HttpResponse(json.dumps(DAOHelper.editRoleInfo(params)))

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
    
    return HttpResponse(json.dumps(DAOHelper.inviteUser(params)))
    
def deleteUser(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1   #default!!!
    params["id"] = request.POST["id"]                               #delete user id
    
    return HttpResponse(json.dumps(DAOHelper.deleteRole(params))) 



def addGroup(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1   #default!!!
    params["groupName"] = request.POST["groupName"]
    
    return HttpResponse(json.dumps(DAOHelper.addGroup(params)))

def editGroup(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1   #default!!!
    params["gid"] = request.POST["gid"]
    params["gname"] = request.POST["gname"]
    
    return HttpResponse(json.dumps(DAOHelper.editGroup(params)))

def deleteGroup(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1   #default!!!
    params["gid"] = request.POST["gid"]
    
    return HttpResponse(json.dumps(DAOHelper.deleteGroup(params)))



def addTag(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1   #default!!!
    params["tagName"] = request.POST["tagName"]
    
    return HttpResponse(json.dumps(DAOHelper.addTag(params)))

def deleteTag(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1   #default!!!
    params["tid"] = request.POST["tid"]                            #delete tag id
    
    return HttpResponse(json.dumps(DAOHelper.deleteTag(params)))



def queryPerson(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1   #default!!!
    params["gid"] = request.GET["gid"]
    params["tid"] = request.GET["tid"]
    
    #hard code
    personList = []
    for i in range(0, 10):
        person = {}
        person["id"] = i + 1
        person["name"] = "Person" + str(i + 1)
        person["sex"] = 1
        personList.append(person)

    return HttpResponse(json.dumps(DAOHelper.queryPerson(params)))


