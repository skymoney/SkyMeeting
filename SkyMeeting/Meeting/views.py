# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
import simplejson as json

def boards(request):
    return render_to_response('404.html')

def meetings(reqeust):
    return render_to_response('meetingList.html')

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
    result = dict()
    result["success"] = "true"
    result["commentId"] = 100
    result["authorId"] = 1
    result["authorName"] = "xxx"
#    exception
#    result["success"] = "false"
#    result["errors"] = ""
    
    return HttpResponse(json.dumps(result))

