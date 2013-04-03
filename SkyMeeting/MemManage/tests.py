"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import simplejson as json

class MemberTest(TestCase):
    def testAllMembers(self):
        response=self.client.get("/members/")
        
        #print response
        self.assertEqual(200,response.status_code,"Get Response Properly")
    
    def testAddGroup(self):
        #response=self.client.get('/members/',{'gid':'1','tid':'1+2'})
        
        #response=self.client.post("/members/addgroup/",{"groupName":"test"})
        #print response.content
        #result=json.loads(response.content)
        #self.assertEqual("true",result["success"],"Add Group Test Done...")
        pass
    
    def tstInviteRole(self):
        from MemManageHelper import DAOHelper as helper
        params=dict()
        params["cid"]=1
        params["name"]="PyUnitTest"
        params["idcard"]="32431432152"
        params["phone"]="123142334"
        params["email"]="saj@sfakl"
        
        params["verifyMode"]="1+2+9"
        params["verifyQuestion"]="Hello"
        params["verifyAnswer"]="World!"
        
        result=helper.inviteUser(params)
        print result
        self.assertEquals("true",result["success"],"TestDone")
        
    def tstDeteleTag(self):
        from MemManageHelper import DAOHelper as helper
        param=dict()
        param["cid"]=1
        param["tid"]=26
        
        result=helper.deleteTag(param)
        print result
        self.assertEqual("true",result["success"],"TestTag")
    
    def testEditGroup(self):
        from MemManageHelper import DAOHelper as helper
        param=dict()
        param["cid"]=1
        param["gid"]=1
        param["gname"]="test"
        result=helper.editGroup(param)
        print result
        self.assertEqual("true",result["success"],"Test Edit Group")