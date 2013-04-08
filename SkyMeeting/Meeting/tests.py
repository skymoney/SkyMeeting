"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class MeetingTest(TestCase):
    def testMeetings(self):
        params=dict()
        params['rid']=1
        #params['type']=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getPartMeetings(params)
    
    def testGetCreateMeeting(self):
        params=dict()
        params['rid']=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getCreateMeeting(params)
        