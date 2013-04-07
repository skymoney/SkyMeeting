#-*-coding:utf-8-*-
'''
Description:provide ops with db and controller layer
        with Meeting module


@author: cheng
'''

from MemManage.models import *
from Meeting.models import *


def meetings(params):
    '''
    get meetings given params
    params:
        permission: user permission
        rid: role id to specify meeting
        type: specified meeting type
    '''
    meetingSet=Meeting_Participant.objects.filter(role_id=params["rid"]).distinct()
    meetingIdList=[]
    #get all id set related to role
    for meeting_single in meetingSet:
        meetingIdList.append(meeting_single.meeting_id_id)
    
    meetingResult=Meeting.objects.filter(meeting_id__in=meetingIdList)
    if "type" in params and params["type"]!="-1":
        typeNum=params["type"]
        meetingResult=meetingResult.filter(meeting_type=typeNum)
    
    #query for file attachment
    return meetingResult
    