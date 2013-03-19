# Create your views here.
from django.shortcuts import render_to_response
def member(request):
    return render_to_response('members.html')

