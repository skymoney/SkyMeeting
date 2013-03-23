"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import simplejson as json

class MemberTest(TestCase):
    def testAllMembers(self):
        #response=self.client.get("/members/")
        
        #print response
        self.assertFalse(1==2,"Done")
    
    def testAddGroup(self):
        #response=self.client.get('/members/',{'gid':'1','tid':'1+2'})
        
        response=self.client.post("/members/addgroup/",{"groupName":"test"})
        print response.content
        result=json.loads(response.content)
        self.assertEqual("true",result["success"],"Add Group Test Done...")