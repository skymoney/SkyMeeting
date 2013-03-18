# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

#just for simple page show
def welcome(request):
    return render_to_response('login.html')

def login(request):
    return HttpResponseRedirect('/meetlist')

def memlist(request):
    return render_to_response('meetingList.html')

