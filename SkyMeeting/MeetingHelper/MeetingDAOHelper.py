#-*-coding:utf-8-*-
'''
Description:provide ops with db and controller layer
        with Meeting module


@author: cheng
'''

from MemManage.models import *
from Meeting.models import *

import BasicUtil as util

def meetings(params):
    '''
    get meetings
    if use url to get meetings,this will be called
    or the following two method will be called
    '''
    if "ad" in params and params["ad"]=="1":
        return getCreateMeeting(params)
    else:
        return getPartMeetings(params)

def getPartMeetings(params):
    '''
    get meetings given params
    meeting role participates
    params:
        permission: user permission
        rid: role id to specify meeting
        type: specified meeting type
    
    @return: result=dict()
    
    '''
    meetingSet=Meeting_Participant.objects.filter(role_id=params["rid"]).distinct()
    meetingIdList=[]
    finalResult=dict()
    finalResult["type"]="-1"
    #get all id set related to role
    for meeting_single in meetingSet:
        meetingIdList.append(meeting_single.meeting_id_id)
    
    meetingData=Meeting.objects.filter(meeting_id__in=meetingIdList)
    if "type" in params and params["type"]!="-1":
        typeNum=params["type"]
        meetingData=meetingData.filter(meeting_type=typeNum)
        finalResult["type"]=params["type"]    
    
    #query for file attachment
    
    finalResult["meetingData"]=util.query2List(meetingData)
    finalResult["ad"]="0"
    
    return finalResult

def getCreateMeeting(params):
    '''
    get meeting who createed 
    '''
    rid=params["rid"]
    finalResult=dict()
    finalResult['type']="-1"
    meetingData=Meeting.objects.filter(create_user=rid)
    if "type" in params and params["type"]!="-1":
        #if type specified, filter specified meetings
        meetingData=meetingData.filter(meeting_type=params["type"])
        finalResult['type']=params['type']    
    
    #more return values can be put here
    finalResult["meetingData"]=util.query2List(meetingData)    
    finalResult['ad']="1"   #return whether create or participate
    
    return finalResult

def uploadFile(params):
    '''
    upload file
    '''
    pass