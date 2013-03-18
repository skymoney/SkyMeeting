# Create your views here.
from django.shortcuts import render_to_response

def meeting(reqeust):
    return render_to_response('meeting.html')

def newMeeting(request):
    return render_to_response('newMeeting.html')