# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login

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
		return HttpResponse('fuck');

def logout(request):
    pass

def memlist(request):
    return render_to_response('meetingList.html')

def home(request):
   if request.user.is_authenticated():
        return render_to_response('meetingList.html')
   else:
        return HttpResponseRedirect('/')

