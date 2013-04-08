"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class MeetingTest(TestCase):
    def tstMeetings(self):
        params=dict()
        params['rid']=1
        #params['type']=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getPartMeetings(params)
    
    def tstGetCreateMeeting(self):
        params=dict()
        params['rid']=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getCreateMeeting(params)
        
    def testGetSingleMeetingInfo(self):
        params=dict()
        params["mid"]=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getSingleMeeting(params)