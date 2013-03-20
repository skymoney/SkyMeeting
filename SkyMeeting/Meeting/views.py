# Create your views here.
from django.shortcuts import render_to_response

def boards(request):
    return render_to_response('404.html')

def meetings(reqeust):
    return render_to_response('meetingList.html')

def newMeeting(request):
    return render_to_response('newMeeting.html')

def documents(request):
    return render_to_response('404.html')