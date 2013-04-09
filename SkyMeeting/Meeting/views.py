# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from MeetingHelper import MeetingDAOHelper
import simplejson as json

def boards(request):
    return render_to_response('404.html')

def documents(request):
    return render_to_response('404.html')



def meetings(request):
    #permission check
    #......
    params = dict()
    params["rid"] = 1 #default!!!
    if "ad" in request.GET:
        params["ad"] = request.GET["ad"]        # 1 for my created meetings, 0 for my attended meetings
    if "type" in request.GET:
        params["type"] = request.GET["type"]    # -1 for all meetings, 1 for formal, 2 for informal
    
    return render_to_response('meetingList.html', Context(MeetingDAOHelper.meetings(params)))

def newMeeting(request):
    return render_to_response('newMeeting.html')

def addMeeting(request):
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
    params["files"] = "???"
    
    return HttpResponse(json.dumps(MeetingDAOHelper.addMeeting(params)))
    
def meeting(request):
    #permission check
    #......
    params = dict()
    params["mid"] = request.GET["mid"]
    return render_to_response('meeting.html', Context(MeetingDAOHelper.getSingleMeeting(params)))

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

