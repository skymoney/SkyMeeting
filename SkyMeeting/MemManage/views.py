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
    u_list=Role.objects.filter(company_id=1)
    conf={}
    if "name" in request.GET:
        #get detail person info
        pass
    elif "gid" in request.GET and "tid" in request.GET:
        #has gid and tid
        #urlFormat: /members/?gid=1&tid=1+2
        if int(request.GET["gid"])>0:
            u_list=Role.objects.filter(company_id=1,groups__id=request.GET["gid"],tags__id__in=request.GET["tid"].split())
            conf["current_gid"]=request.GET['gid']
            conf["current_tid"]=request.GET['tid'].split()
        else:
            u_list=Role.objects.filter(company_id=1,tags__id__in=request.GET["tid"].split())
            
    elif "gid" in request.GET:
        #only has gid
        #urlFormat: /members/?gid=1
        if int(request.GET["gid"])>0:
            conf["current_gid"]=request.GET['gid']
            u_list=Role.objects.filter(company_id=1,groups__id=request.GET["gid"])
        #return HttpResponse(u_list)
    elif "tid" in request.GET:
        #only has tig
        #urlFormat: /members/?tid=1+2
        tagSet=request.GET["tid"].split()
        conf["current_tid"]=tagSet
        u_list=Role.objects.filter(company_id=1,tags__id__in=tagSet)
        #return HttpResponse(u_list)
    #get all users
    # company_id is passed from request
    
    g_list=Group.objects.filter(cid=1)
    t_list=Tag.objects.filter(cid=1)
    groupList=[]
    tagList=[]
    for tag in t_list:
        singleTag={}
        singleTag["tid"]=tag.id
        singleTag["tname"]=tag.tname
        singleTag["cid"]=tag.cid_id
        tagList.append(singleTag)
    print json.dumps(tagList)
    #here can optimize by just sql query instead of Model method
    for g in g_list:
        singleGroup={}
        num=len(Role.objects.filter(company_id=1,groups__id=g.id))
        singleGroup["gid"]=g.id
        singleGroup["gname"]=g.gname
        singleGroup["cid"]=g.cid_id
        singleGroup["count"]=num
        groupList.append(singleGroup)
    #conf can set more values here
    
    return render_to_response('members.html',Context({"groupAll":groupList,"groupString":json.dumps(groupList),"tagAll":t_list,"memberAll":u_list,"groupAllCount":len(u_list),"tagString":json.dumps(tagList),"conf":conf}))


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
    #here can be optimized by sql query insteas of model method
    
    
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
