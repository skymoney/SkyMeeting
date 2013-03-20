# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Login.models import Account

#just for simple page show
def welcome(request):
    return render_to_response('login.html')

def login(request):
    if request.session.get("login",False):
        return HttpResponseRedirect('/meetlist')
    else:
        uname=request.POST["username"]
        upass=request.POST["password"]
        account=Account.objects.filter(aname=uname,apassword=upass)
        if len(account)>0:
            request.session["login"]=True
            if uname=="admin":             
                   
                request.session["info"]="1"
            else:
                request.session["info"]="0"
            return HttpResponseRedirect('/meetlist')
        else:
            return HttpResponseRedirect('/')

def memlist(request):
    
    return render_to_response('meetingList.html')

