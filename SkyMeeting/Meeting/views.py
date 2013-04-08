# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from MeetingHelper import MeetingDAOHelper
import simplejson as json

def boards(request):
    return render_to_response('404.html')

def meetings(request):
    #permission check
    #......
    params = dict()
    params["rid"] = 1 #default!!!
    if "ad" in request.GET:
        params["ad"] = request.GET["ad"]
    if "type" in request.GET:
        params["type"] = request.GET["type"]
    
    return render_to_response('meetingList.html', Context(MeetingDAOHelper.meetings(params)))

def documents(request):
    return render_to_response('404.html')

def newMeeting(request):
    return render_to_response('newMeeting.html')

def meeting(request):
    return render_to_response('meeting.html')

def addComment(request):
    #permission check
    #......
    params = dict()
    params["meetingId"] = request.POST["meetingId"]
    params["userId"] = 1                                            #get from session
    params["time"] = ""                                             #get current time
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
    
    result = dict()
    result["success"] = "true"
    result["commentId"] = 100
    result["authorId"] = 1
    result["authorName"] = "Tony Jiong"
    result["createTime"] = "2013/4/6 15:21"
    result["headUrl"] = "???"
#    exception
#    result["success"] = "false"
#    result["errors"] = ""
    
    return HttpResponse(json.dumps(result))

