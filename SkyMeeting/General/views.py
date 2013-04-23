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
    result = dict()
    result["dashboards"] = GeneralHelper.getDashboard(request.user)
    result["langPack"] = RequestUtil.getLangPack(request)
    result["rolePack"] = RequestUtil.getRolePack(request)
    result["authPack"] = RequestUtil.getAuthPack(request)
    return render_to_response('home.html', Context(result))


@login_required
def profile(request):
    #暂且矬比
    request.user.last_login = request.user.last_login.strftime("%Y/%m/%d %H:%M")
    request.user.date_joined = request.user.date_joined.strftime("%Y/%m/%d %H:%M")
    ########
    params = dict()
    params["rid"] = request.session["rid"]
    
    result = dict()
    result["profile"] = GeneralHelper.getProfile(params)
    result["account"] = request.user
    result["langPack"] = RequestUtil.getLangPack(request)
    result["rolePack"] = RequestUtil.getRolePack(request)
    result["authPack"] = RequestUtil.getAuthPack(request)
    return render_to_response('profile.html', Context(result))

@login_required
def editProfile(request):
    params = dict()
    params["rid"] = request.session["rid"]
    params["name"] = request.POST["name"]
    params["sex"] = request.POST["sex"]
    params["idcard"] = request.POST["idcard"]
    params["phone"] = request.POST["phone"]
    params["email"] = request.POST["email"]
    
    GeneralHelper.editProfile(params)
    return HttpResponseRedirect('/profile')

@login_required
def editAccount(request):
    params = dict()
    params["aid"] = request.user.aid
    params["oldPwd"] = request.POST["oldPassword"]
    params["newPwd"] = request.POST["newPassword"]
    return HttpResponse(json.dumps(GeneralHelper.changePwdInner(params)))



@login_required
def changeCurRid(request):
    if request.method=="POST":
        newRid=request.POST["rid"]
        newCid=request.POST["cid"]
        request.session["rid"]=newRid
        request.session["cid"]=newCid
        
        from MemManage.models import Role
        request.session["rlevel"] = Role.objects.get(rid=newRid).permission
        return HttpResponseRedirect('/meetings')



@login_required
def documents(request):
    return render_to_response('404.html')

def error(request):
    return render_to_response('500.html')



def forgetPassword(request):
    params = dict()
    params["email"] = request.POST["email"]
    return HttpResponse(json.dumps(GeneralHelper.changePwdViaEmail(params)))
    
