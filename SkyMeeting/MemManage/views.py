#-*-coding:utf-8-*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from MemManage.models import Role
from MemManage.models import Group
from MemManage.models import Tag
from MemManage.models import Company
import simplejson as json

def member(request):
    if "name" in request.GET:
        #get detail person info
        pass
    if "gid" in request.GET and "tid" in request.GET:
        #has gid and tid
        #urlFormat: /members/?gid=1&tid=1+2
        pass
    if "gid" in request.GET:
        #only has gid
        #urlFormat: /members/?gid=1
        u_list=Role.objects.filter(company_id=1,groups_id=request.GET["gid"])
        return HttpResponse(u_list)
    if "tid" in request.GET:
        #only has tig
        #urlFormat: /members/?tid=1+2
        pass
    #get all users
    # company_id is passed from request
    u_list=Role.objects.filter(company_id=1)
    g_list=Group.objects.filter(cid=1)
    t_list=Tag.objects.filter(cid=1)
    groupList=[]
    #here can optimize by just sql query instead of Model method
    for g in g_list:
        singleGroup={}
        gid=g.id
        num=len(Role.objects.filter(company_id=1,groups__id=gid))
        singleGroup["id"]=g.id
        singleGroup["gname"]=g.gname
        singleGroup["cid"]=g.cid
        singleGroup["count"]=num
        groupList.append(singleGroup)
    return render_to_response('members.html',Context({"groupAll":groupList,"tagAll":t_list,"memberAll":u_list,"groupAllCount":len(u_list),"tagString":Tag.objects.getAllString(1)}))


def editRoleInfo(request):
    #save specified role info
    #here add permission 
    '''
     id,            role的id
                     name,
                     sex,
                     idcard,
                     phone,
                     email,
                     //location,    先不用
                     groupIds,        e.g. 1+2+3
                     tagIds            e.g. 1+2+3
                     '''
    roleid=request.POST["id"]
    role=Role.objects.get(id=roleid)
    role.name=request.POST["name"]
    role.sex=int(request.POST["sex"])
    role.idcard=request.POST["idcard"]
    role.phone=request.POST["phone"]
    role.email=request.POST["email"]
    
    groupIds=request.POST["groupIds"].split('+')
    tagIds=request.POST["tagIds"].split('+')
    
    result=dict()
    try:
        role.save()
        result["success"]="true"
        return HttpResponse(json.dumps(result))
    except:
        result["success"]="false"
        result["errorcode"]=""  #add error status
        result["error"]=""
        return HttpResponse(json.dumps(result))

def addGroup(request):
    #add new group
    gname=request.POST('groupName')
    #here add permission deal
    ng=Group()
    ng.gname=gname
    ng.cid=Company.objects.get(cid=request.POST["cid"])
    result=dict()
    try:
        ng.save()
        ng_id=ng.id()
        result["success"]="true"
        result["gid"]=ng_id
        return HttpResponse(json.dumps(result))
    except:
        result["success"]="false"
        result["error"]=""  #describe error status
        result["errorcode"]=""
        return HttpResponse(json.dumps(result))

def addTag(request):
    tname=request.POST["tagName"]
    nt=Tag()
    nt.tname=tname
    nt.cid=Company.objects.get(cid=request.POST["cid"])
    result=dict()
    try:
        nt.save()
        nt_id=nt.id()
        result["success"]="true"
        result["tid"]=nt_id
        return HttpResponse(json.dumps(result))
    except:
        result["success"]="fasle"
        result["error"]=""  #descript error status
        result["errorcode"]=""
        return HttpResponse(json.dumps(result))
