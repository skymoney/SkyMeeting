#-*- coding:utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from GeneralHelper import GeneralHelper
from GlobalUtil import RequestUtil
import simplejson as json
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    params = dict()
    params["rid"] = 1 #default!!!
    params["cid"] = 1 #default!!!
    
    dashboards = GeneralHelper.getDashboard(request.user)
    result = dict()
    result["dashboards"] = dashboards
    result["langPack"] = RequestUtil.getLangPack(request)
    
    rolePack = dict()
    rolePack["roles"] = RequestUtil.getRolePack(request)
    rolePack["curRid"] = request.session["rid"]if "rid" in request.session else request.user.role_set.all()[0].rid
    
    result["rolePack"] = rolePack
    
    return render_to_response('home.html', Context(result))


@login_required
def profile(request):
    params = dict()
    params["rid"] = 1 #default!!!
    
    result = GeneralHelper.getProfile(params)
    result["langPack"] = RequestUtil.getLangPack(request)
    return render_to_response('profile.html', Context(result))

@login_required
def editProfile(request):
    params = dict()
    params["rid"] = 1 #default!!!
    params["name"] = request.POST["name"]
    params["sex"] = request.POST["sex"]
    params["idcard"] = request.POST["idcard"]
    params["phone"] = request.POST["phone"]
    params["email"] = request.POST["email"]
    
    GeneralHelper.editProfile(params)
    return HttpResponseRedirect('/profile')


@login_required
def documents(request):
    return render_to_response('404.html')

@login_required
def changeCurRid(request):
    if request.method=="POST":
        newRid=request.POST["rid"]
        #from MemManage.models import Role
        #if len(Role.objects.get(request.session["rid"]).account.role_set.filter(rid=newRid)):
        request.session["rid"]=newRid
        return HttpResponseRedirect('/meetings')
