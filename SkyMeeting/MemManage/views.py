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
    
    #get all users
    # company_id is passed from request
    u_list=Role.objects.filter(company_id=1)
    g_list=Group.objects.filter(cid=1)
    t_list=Tag.objects.filter(cid=1)
    return render_to_response('members.html',Context({"groupAll":g_list,}))


#get user,default get all users
def getUser(request):
    #print 'Request'
    u_list=Role.objects.all()  #get all user by specifying cid
    
    #print len(u_list)
    return render_to_response("members.html",Context({"memberAll":u_list,"test":""}))
    #return render_to_response('members.html')

#get user by given groupid and cid
def getUserByGroup(request,gid):
    
    pass

#get user by given tag id(s) and cid
def getUserByTag(request):
    pass



