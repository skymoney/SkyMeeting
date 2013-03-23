#-*-coding:utf-8-*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
import simplejson as json

from MemManage.models import Role
from MemManage.models import Group
from MemManage.models import Tag
from MemManage.models import Company

import BasicUtil as util

def member(request):
    u_list=Role.objects.filter(company_id=1)
    RoleCount=len(u_list)
    #def conf variable to store current 
    #groups and tags info
    conf={}
    conf["current_gid"]=-1
    conf["current_tid"]=-1
    
    if 'gid' in request.GET and len(request.GET['gid'])>0:
        if request.GET['gid']=="-1":
            pass
        else:
            try:
                u_list=u_list.filter(groups__id=int(request.GET['gid']))
                conf['current_gid']=int(request.GET['gid'])
            except:
                pass
    if 'tid' in request.GET and len(request.GET['tid'])>0:
        if '-1' in request.GET['tid'].split():
            pass
        else:
            try:
                u_list=u_list.filter(tags__id__in=(request.GET['tid'].split()))
                conf['current_tid']=util.listToInt(request.GET['tid'].split())
            except:
                pass
       
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
    
    return render_to_response('members.html',Context({"groupAll":groupList,"groupString":json.dumps(groupList),"tagAll":t_list,"memberAll":u_list,"groupAllCount":RoleCount,"tagString":json.dumps(tagList),"conf":conf}))



def editRoleInfo(request):
    #save specified role info
    #here add permission 
    result=dict()
    try:
        roleid=int(request.POST["id"])
        Role.objects.filter(id=roleid).update(
                     name=request.POST["name"],
                     sex=int(request.POST["sex"]),
                     idcard=request.POST["idcard"],
                     phone=request.POST["phone"],
                     email=request.POST["email"])
        #clear all original groups and tags
        Role.objects.get(id=roleid).groups.clear()
        Role.objects.get(id=roleid).tags.clear()
        
        #here can be optimized by sql query instead of model method
        if len(request.POST["groupIds"])>0:
            groupIds=request.POST["groupIds"].split('+')
            for group in groupIds:
                Role.objects.get(id=roleid).groups.add(int(group))
        if len(request.POST['tagIds'])>0:
            tagIds=request.POST["tagIds"].split('+')
            for tag in tagIds:
                Role.objects.get(id=roleid).tags.add(int(tag))
        result["success"]="true"
        return HttpResponse(json.dumps(result))
    except:
        result["success"]="false"
        result["errorcode"]=""  #add error status
        result["error"]=""
        return HttpResponse(json.dumps(result))

def addGroup(request):
    #add new group
    gname=request.POST['groupName']
    #here add permission deal
    ng=Group()
    ng.gname=gname
    ng.cid=Company.objects.get(id=1)
    result=dict()
    try:
        ng.save()
        ng_id=ng.id
        result["success"]="true"
        result["gid"]=ng_id
        return HttpResponse(json.dumps(result))
    except:
        result["success"]="false"
        result["error"]=""  #describe error status
        result["errorcode"]=""
        return HttpResponse(json.dumps(result))

def addTag(request):
    #add new tag
    tname=request.POST["tagName"]
    nt=Tag()
    nt.tname=tname
    nt.cid=Company.objects.get(id=1)
    result=dict()
    try:
        nt.save()
        nt_id=nt.id
        result["success"]="true"
        result["tid"]=nt_id
        return HttpResponse(json.dumps(result))
    except:
        result["success"]="fasle"
        result["error"]=""  #descript error status
        result["errorcode"]=""
        return HttpResponse(json.dumps(result))
