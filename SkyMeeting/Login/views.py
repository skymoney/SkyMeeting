#-*- coding:utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from LoginHelper import LoginHelper
from MemManage.models import TempRole,Role  
from Login.models import Account 
import simplejson


#just for simple page show
def welcome(request):
    if "rid" not in request.session:
        if "next" in request.GET:
            redirectUrl=request.GET['next']
        else:
            redirectUrl="/home"
        return render_to_response('login.html',{"redirectUrl":redirectUrl})
    else:
        return HttpResponseRedirect('/dashboard')

def login(request):
    user = authenticate(username=request.POST['accountname'], password=request.POST['password']);
    if user is not None:
        # Redirect to a success page.
        auth_login(request,user)
        role=user.role_set.all()[0]
        request.session["rid"]=role.rid
        request.session["cid"]=role.company_id
        request.session["rlevel"]=role.permission
        return HttpResponseRedirect(request.POST['redirectUrl'])
    else:
        # Return an error message.
        return HttpResponseRedirect('/')

def logout(request):
    '''
    user logout
    del session and redirect to welcome page
    '''
    auth_logout(request)
    return HttpResponseRedirect('/')

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/')



def invite(request):
    try :
        #get the invite code
        invitecode = request.GET['code']
    except Exception:
        return HttpResponseRedirect('/')
    try :
        #check whether invitecode is legal
        tempRole = TempRole.objects.get(code = invitecode)
    except TempRole.DoesNotExist:
        return HttpResponse('Your invite code is not legal!')
    
    request.session['code'] = invitecode
    params = dict()
    params["code"] = invitecode
    return render_to_response('invite.html', Context(LoginHelper.fetcheVerifyInfo(params)))

def register(request):
    '''
    register with an already existed account
    '''
    params = dict()
    params["create"] = "false"
    params["code"] = request.session['code']
    params["aname"] = request.POST["accountname"]
    params["apass"] = request.POST["password"]
    
    result = LoginHelper.confirmRole(params)
    if result["success"] == "true":
        del request.session["code"]
        #以下代码同login
        user = authenticate(username=params["aname"], password=params["apass"]);
        if user is not None:
            auth_login(request,user)
            request.session["rid"]=result["rid"]
            request.session["cid"]=result["cid"]
            request.session["rlevel"]=result["rlevel"]
            return HttpResponseRedirect('/profile')
        
    # Return an error message.
    return HttpResponseRedirect('/')

def registerNewAccount(request):
    '''
    register and create a new account
    '''
    params = dict()
    params["create"] = "true"
    params["code"] = request.session['code']
    params["aname"] = request.POST["accountname"]
    params["apass"] = request.POST["password"]
    
    if "name" in request.POST:
        params["verifyName"] = request.POST["name"]
    if "idcard" in request.POST:
        params["verifyIdcard"] = request.POST["idcard"]
    if "answer" in request.POST:
        params["verifyAnswer"] = request.POST["answer"]
    
    result = LoginHelper.confirmRole(params)
    if result["success"] == "true":
        print "confirm success"
        del request.session["code"]
        #以下代码同login
        user = authenticate(username=params["aname"], password=params["apass"]);
        if user is not None:
            auth_login(request,user)
            request.session["rid"]=result["rid"]
            request.session["cid"]=result["cid"]
            request.session["rlevel"]=result["rlevel"]
            return HttpResponseRedirect('/profile')
    
    # Return an error message.
    print result["errors"]
    return HttpResponseRedirect('/')



def regedit(request):
    if request.method == 'POST':  
        username = request.POST['accountname']  
        password = request.POST['password']  
        #email = request.POST['email']
        trueName = request.POST['trueName']
        idCard = request.POST['idCard']
        
        #add verification of trueName and idCard here
        #todo
        
        
        user = Account.objects.create_user(username = username, password = password)  
        if user is not None:
            #Validation success
            user.save()
            tempRole =  TempRole.objects.get(code = request.session['code'])
            role = Role.objects.create(name= tempRole.name,idcard=tempRole.idcard,phone=tempRole.phone,email=tempRole.email,aid=user,company=tempRole.company)
            tempRole.delete()
            role.save()
            del request.session['code']
            return HttpResponse(simplejson.dumps({'msg':'ok'}))  
        else:  
            return HttpResponse(simplejson.dumps({'msg':'fail'})) 
   
    
def memlist(request):
    return render_to_response('meetingList.html')

