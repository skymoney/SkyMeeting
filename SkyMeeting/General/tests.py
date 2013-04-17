#-*- coding:utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class GeneralTest(TestCase):
    def testEditProfile(self):
        params=dict()
        params["rid"]=3
        params["name"]="艹"
        params["sex"]="1"
        params["phone"]="13234"
        params["email"]="fd@fsd.com"
        params["idcard"]="241432534"
        
        from GeneralHelper.GeneralHelper import editProfile
        print editProfile(params)