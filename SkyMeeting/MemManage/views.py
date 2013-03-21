# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from MemManage.models import Role
from MemManage.models import Group
from MemManage.models import Tag

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
    return render_to_response('members.html',Context({"groupAll":groupList,"tagAll":t_list,"memberAll":u_list,"groupAllCount":len(u_list)}))


def saveRoleInfo(request):
    #save specified role info
    pass


