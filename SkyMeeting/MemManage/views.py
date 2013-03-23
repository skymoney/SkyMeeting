#-*-coding:utf-8-*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from MemManageHelper import DAOHelper
import simplejson as json

def member(request):
    #member ops including visiting
    return render_to_response('members.html',Context(DAOHelper.member(request)))

def editRoleInfo(request):
    #save specified role info
    return HttpResponse(json.dumps(DAOHelper.editRoleInfo(request)))    

def addGroup(request):
    #add new group    
    return HttpResponse(json.dumps(DAOHelper.addGroup(request)))

def addTag(request):
    #add new tag
    return HttpResponse(json.dumps(DAOHelper.addTag(request)))
