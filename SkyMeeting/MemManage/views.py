# Create your views here.
from django.shortcuts import render_to_response
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
        pass
    if "tid" in request.GET:
        #only has tig
        #urlFormat: /members/?tid=1+2
        pass
    #get all users
    # company_id is passed from request
    u_list=Role.objects.filter(company_id=1)
    g_list=Group.objects.filter(cid=1)
    t_list=Tag.objects.filter(cid=1)
    
    groupNum={}
    for g in g_list:
        gid=g.id
        num=len(Role.objects.filter(company_id=1,groups__id=gid))
        groupNum[str(gid)]=num
    return render_to_response('members.html',Context({"groupAll":g_list,"tagAll":t_list,"memberAll":u_list,"groupNum":groupNum}))


#get user by given groupid and cid
def getUserByGroup(request,gid):
    
    pass

#get user by given tag id(s) and cid
def getUserByTag(request):
    pass



