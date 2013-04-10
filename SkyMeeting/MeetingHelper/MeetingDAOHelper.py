#-*-coding:utf-8-*-
'''
Description:provide ops with db and controller layer
        with Meeting module


@author: cheng
'''

from MemManage.models import *
from Meeting.models import *
from datetime import datetime,timedelta
import BasicUtil as util
from GlobalUtil import DataUtil

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
    @param file: file Set object
    '''
    fileSet=params["file"]
    finalResultSet=[]
    for f in fileSet:
        finalResult=dict()    
        result=util.handleFile(f)
        if result["success"]=="true":
            fileTb=File()
            fileTb.file_path=result["path"]
            fileTb.file_name=f.name
            fileTb.file_size=f.size
            fileTb.upload_user=Role.objects.get(rid=params["rid"])
            fileTb.upload_time=datetime.now()
            fileTb.file_status=0
            try:
                fileTb.save()
                finalResult["success"]="true"
                finalResult["fildId"]=fileTb.file_id
            except:
                finalResult["success"]="false"
                finalResult["errors"]=""
        else:
            finalResult["success"]="false"
            finalResult["errors"]=""
        finalResultSet.append(finalResult)
    return finalResultSet

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
    finalResult["meetingComment"]=fetchComment(params)["comment"]
    return finalResult

def addMeeting(params):
    '''
    create a new meeting
    '''
    meeting=Meeting()
    result=dict()
    meeting.meeting_title=params["title"]
    meeting.meeting_type=int(params["type"])
    meeting.start_time=datetime.strptime(params["startTime"],"%Y/%m/%d %H:%M")
    meeting.meeting_period=12       #current default 12
    meeting.close_time=meeting.start_time+timedelta(days=7) #default start_time plus 7 days
    meeting.meeting_place=params["place"]
    meeting.contact_tel=params["tel"]
    meeting.contact_email=params["email"]
    meeting.detail=params["detail"]
    meeting.create_user=Role.objects.get(rid=params["createUser"])
    meeting.create_time=datetime.now()      #default current time
    meeting.meeting_status=1        #meeting_status 1 or 0 or more..
    
    try:
        meeting.save()      #save meeting info
        #save participant info
        #currently not include create_user,just users who will participate
        if "participants" in params:
            roleIdSet=params["participants"].split('+')
            for roleId in roleIdSet:
                Meeting_Participant(meeting_id=meeting,role_id=Role.objects.get(rid=roleId),participant_status=0).save()
        if "file" in params:
            #store file info
            #currently not done...
            pass
        
        result["success"]="true"
        result["mid"]=meeting.meeting_id
    except:
        result["success"]="false"
    
    return result

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
    commentObj.create_time=datetime.now()
    commentObj.content=params["content"]
    try:
        commentObj.reply_to_user=int(params["replyToUser"])
    except:
        pass
    commentObj.comment_status=0     #default 0
    try:
        commentObj.quote_from_comment_id=int(params["replyToComment"])
    except:
        pass
    
    try:
        commentObj.save()
        result["success"]="true"  
        result["commentId"]=commentObj.comment_id
        result["authorId"]=commentObj.create_user.rid
        result["authorName"]=commentObj.create_user.name
        result["createTime"]=commentObj.create_time.strftime("%Y/%m/%d %H:%M")
        result["headUrl"]=""
    except:
        result["success"]="false"
        result["errors"]=""
    
    return result
    
def fetchComment(params):
    '''
    fetch all comments given specified company lid
    '''
    #may be paging after
    commentList=Meeting_Comment.objects.filter(meeting_id=params["mid"]).distinct()
    
    finalResult=dict()
    finalResult["comment"]=util.comment2List(commentList)
    
    return finalResult

def newMetingInitial(params):
    '''
    create new meeting initial info
    Group and Tag are needed to initialize page
    @param cid: company id
    '''
    #getAllGroups()
    g_list=Group.objects.filter(company_id=params["cid"])
    groupList=DataUtil.getGroupList(g_list)
    
    t_list=Tag.objects.filter(company_id=params["cid"])
    tagList=DataUtil.getTagList(t_list)
    
    finalResult=dict()
    
    finalResult["groupAll"]=groupList
    finalResult["tagAll"]=tagList
    
    return finalResult