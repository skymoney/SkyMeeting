# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from MemManage.models import TempRole,Role  
from Login.models import Account 

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
    pass

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
	if request.method == 'GET':  
        username = request.GET['username']  
        password = request.GET['password']  
        email = request.GET['email']
		trueName = request.GET['trueName']
		idCard = request.GET['idCard']
        user = Account.objects.create_user(username, password)  
        if user is not None:
			#Validation success
            user.save()
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

