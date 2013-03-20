# Create your views here.
from django.shortcuts import render_to_response
from django.template import Context
from MemManage.models import Role

def member(request):
    return render_to_response('members.html')


#get user,default get all users
def getUser(request):
    u_list=Role.objects.all()  #get all user by specifying cid
    
    return render_to_response("",Context({"memberAll":u_list}))


#get user by given groupid and cid
def getUserByGroup(request,gid):
    
    pass

#get user by given tag id(s) and cid
def getUserByTag(request):
    pass



