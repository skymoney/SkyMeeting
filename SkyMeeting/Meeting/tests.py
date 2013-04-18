#-*- coding:utf-8 -*-
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
        params["pn"]=1
        #params['type']=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getPartMeetings(params)
    
    def tstGetCreateMeeting(self):
        params=dict()
        params['rid']=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getCreateMeeting(params)
        
    def tstGetSingleMeetingInfo(self):
        params=dict()
        params["mid"]=1
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.getSingleMeeting(params)
    
    def tetAddComment(self):
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
    
    def tstSaveMeeting(self):
        params=dict()
        params["mid"]=1
        params["createUser"] = 1 #default!!!                        # create by user id
        params["title"] = "test Meeting"
        params["type"] = 1
        from datetime import datetime
        params["startTime"] = "2013/3/4 12:00"            # yyyy/mm/dd hh:mm
        params["place"] = "Nanjing"
        params["tel"] = "21243"
        params["email"] = "dfjk@dlsf.com"
        params["detail"] = "None"                   # HTML code
        params["participants"] = "1+2"       # role ids, "1+2+3" etc.
        params["files"] = "1+2"
        
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.saveMeeting(params)
    
    def tstEditStatus(self):
        params=dict()
        params["mid"]=1
        params["status"]="10"
        
        from MeetingHelper import MeetingDAOHelper
        print MeetingDAOHelper.changeMeetingStatus(params)
        