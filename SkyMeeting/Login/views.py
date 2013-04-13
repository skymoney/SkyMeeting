# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from MemManage.models import TempRole,Role  
from Login.models import Account 
import simplejson


#just for simple page show
def welcome(request):
    return render_to_response('login.html')

def login(request):
    user = authenticate(username=request.POST['username'], password= request.POST['password']);
    if user is not None:
        # Redirect to a success page.
        auth_login(request,user)
        return HttpResponseRedirect('/members')
    else:
        # Return an error message.
        return HttpResponse('fuck')

def logout(request):
    '''
    user logout
    del session and redirect to welcome page
    '''
    auth_logout(request)
    return HttpResponseRedirect('/')

def invite(request):
    try :
        #get the invite code
        invitecode = request.GET['code']
    except Exception:
        return HttpResponseRedirect('/')
    try :
        #check whether invitecode is legal
        print invitecode
        tempRole = TempRole.objects.get(code = invitecode) 
    except TempRole.DoesNotExist:
        return HttpResponse('Your invite code is not legal!')
    request.session['code']= invitecode
    return render_to_response('invite.html')
   
       
def regedit(request):
    if request.method == 'POST':  
        username = request.POST['username']  
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

def home(request):
    if request.user.is_authenticated():
        return render_to_response('meetingList.html')
    else:
        return HttpResponseRedirect('/')

def register(request):
    '''
    user register
    '''
    pass
