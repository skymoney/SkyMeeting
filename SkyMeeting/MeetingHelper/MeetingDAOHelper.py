#-*-coding:utf-8-*-
'''
Description:provide ops with db and controller layer
        with Meeting module


@author: cheng
'''

from MemManage.models import *
from Meeting.models import *
from datetime import datetime
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

def getSingleMeeting(params):
    '''
    get single meeting detail info
    given meeting id
    @param mid: meeting id 
    '''
    mid=params["mid"]
    meeting=Meeting.objects.get(meeting_id=mid)
    role_list=Role.objects.filter(meeting_participant__meeting_id=mid)
    finalResult=dict()
    
    finalResult["meetingParticipant"]=util.getMeetingParticipant(role_list)
    finalResult["meetingData"]=util.getSingleMeetingInfo(meeting)
    #add more return values such as file and comment
    return finalResult

def addComment(params):
    '''
    add comment to specified meeting by specified user
    @param meetingId: meeting id
    @param userId: role id
    @param time: when comment posted
    @param content: content of comment
    @param replyToUser: rid of reply comment
    @param replyToComment: reply comment id of this comment
    @param status: status of comment
    '''
    result=dict()
    
    commentObj=Meeting_Comment()
    commentObj.meeting_id=Meeting.objects.get(meeting_id=int(params["meetingId"]))
    commentObj.create_user=Role.objects.get(rid=int(params["userId"]))
    commentObj.create_time=datetime.now().strftime( '%Y-%m-%d %H:%M' )
    commentObj.content=params["content"]
    commentObj.reply_to_user=int(params["replyToUser"])
    commentObj.comment_status=0     #default 0
    commentObj.quote_from_comment_id=int(params["replyToComment"])
    
    try:
        commentObj.save()
        result["success"]="true"        
    except:
        result["success"]="false"
        result["errors"]=""
    
    return result
    