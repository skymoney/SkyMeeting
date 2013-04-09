#-*-coding:utf-8-*-
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
        
    def tetGetSingleMeetingInfo(self):
        params=dict()
        params["mid"]=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getSingleMeeting(params)
    
    def testAddComment(self):
        params=dict()
        params["meetingId"]=1
        params["userId"]=2
        params["content"]="苍天已死，黄天当立。PMCEO，宁有种乎。程序员觉醒吧！！！！"
        params["replyToUser"]=1
        params["replyToComment"]=1
        from MeetingHelper import MeetingDAOHelper
        result=MeetingDAOHelper.addComment(params)
        print result
        self.assertEqual("true",result["success"],"Add Comment done...")
    
    def tetFetchComment(self):
        params=dict()
        params["mid"]=1
        
        from MeetingHelper import MeetingDAOHelper
        
        result=MeetingDAOHelper.fetchComment(params)
        print result
        
        