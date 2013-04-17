#-*- coding:utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from MeetingHelper import MeetingDAOHelper
from GlobalUtil import RequestUtil
import simplejson as json
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    params = dict()
    params["rid"] = 1 #default!!!
    params["cid"] = 1 #default!!!
    
    dashboards = MeetingDAOHelper.getDashboard(request.user)
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
    result = dict()
    result["langPack"] = RequestUtil.getLangPack(request)
    return render_to_response('profile.html', Context(result))

@login_required
def documents(request):
    return render_to_response('404.html')


@login_required()
def meetings(request):
    #permission check
    #......
    params = dict()
    params["rid"] = 1 #default!!!
    if "ad" in request.GET:
        params["ad"] = request.GET["ad"]        # 1 for my created meetings, 0 for my attended meetings
    if "type" in request.GET:
        params["type"] = request.GET["type"]    # -1 for all meetings, 1 for formal, 2 for informal
    
    result = MeetingDAOHelper.meetings(params)
    result["langPack"] = RequestUtil.getLangPack(request)
    return render_to_response('meetingList.html', Context(result))

@login_required
def newMeeting(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1 #default!!!
    
    result = MeetingDAOHelper.newMetingInitial(params)
    result["langPack"] = RequestUtil.getLangPack(request)
    return render_to_response('newMeeting.html', Context(result))

@login_required
def saveMeeting(request):
    #permission check
    #......
    params = dict()
    params["createUser"] = 1 #default!!!                        # create by user id
    params["title"] = request.POST["title"]
    params["type"] = request.POST["type"]
    params["startTime"] = request.POST["startTime"]             # yyyy/mm/dd hh:mm
    params["place"] = request.POST["place"]
    params["tel"] = request.POST["tel"]
    params["email"] = request.POST["email"]
    params["detail"] = request.POST["detail"]                   # HTML code
    params["participants"] = request.POST["participants"]       # role ids, "1+2+3" etc.
    params["files"] = request.POST["files"]                     # file ids, "1+2+3" etc.
    
    if "mid" in request.POST:
        params["mid"] = request.POST["mid"]                     # mid exists when updating
    
    return HttpResponse(json.dumps(MeetingDAOHelper.saveMeeting(params)))

@login_required
def editMeeting(request):
    #permission check
    #......
    params = dict()
    params["cid"] = 1 #default!!!
    params["mid"] = request.GET["mid"] #GET or POST???
    
    tempResult = MeetingDAOHelper.newMetingInitial(params)
    result = MeetingDAOHelper.getSingleMeeting(params)
    result["groupAll"] = tempResult["groupAll"]
    result["tagAll"] = tempResult["tagAll"]
    result["langPack"] = RequestUtil.getLangPack(request)
    return render_to_response('newMeeting.html', Context(result))

@login_required
def deleteMeeting(request):
    #permission check
    #Is this meeting created by the user?
    #......
    params = dict()
    params["mid"] = request.POST["mid"]
    
    result = dict()
    result["success"] = "true"
    return HttpResponse(json.dumps(result))

@login_required 
def meeting(request):
    #permission check
    #......
    params = dict()
    params["mid"] = request.GET["mid"]
    
    result = MeetingDAOHelper.getSingleMeeting(params)
    result["langPack"] = RequestUtil.getLangPack(request)
    return render_to_response('meeting.html', Context(result))

@login_required
def addComment(request):
    #permission check
    #......
    params = dict()
    params["meetingId"] = request.POST["meetingId"]
    params["userId"] = 1                                            #get from session
    params["content"] = request.POST["content"]                     #simple text
    params["replyToUser"] = request.POST["replyToUser"]             #reply to user id
    params["replyToComment"] = request.POST["replyToComment"]       #reply to comment id
    #comment status
    
    #hard code!!!
#    comment = {}
#    comment["commentId"] = "1234"
#    comment["meetingId"] = "1"
#    comment["authorId"] = "1"
#    comment["authorName"] = "Tony Jiong"
#    comment["createTime"] = "2013/4/6 15:21"
#    comment["content"] = request.POST["content"]
#    comment["replyToUser"] = ""
#    comment["commentStatus"] = ""
    
#    result = dict()
#    result["success"] = "true"
#    result["commentId"] = 100
#    result["authorId"] = 1
#    result["authorName"] = "Tony Jiong"
#    result["createTime"] = "2013/4/6 15:21"
#    result["headUrl"] = "???"
    
    return HttpResponse(json.dumps(MeetingDAOHelper.addComment(params)))

@login_required
def uploadFile(request):
    fSet=[]
    for f in request.FILES:
        fSet.append(request.FILES[str(f)])
    
    params=dict()
    params["file"]=fSet
    params["rid"]="1" #default!!!
    
    result=MeetingDAOHelper.uploadFile(params)
    print result
    return HttpResponse(json.dumps(result))
