"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class LoginTest(TestCase):
    def testInsertRole(self):
        params=dict()
        params["create"]="true"
        params["code"]="550a141f12de6341fba65b0ad0433500"
        params['aname']="tests"
        params["apass"]="123456"
        
        params["verifyName"]="qcc"
        
        from LoginHelper import LoginHelper
        print LoginHelper.confirmRole(params)