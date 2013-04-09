'''
Created on 2013-4-8

@author: cheng
'''
import datetime



def query2List(meetingData):
    meetingResult=[]
    
    for meeting in meetingData:
        singleMeeting=dict()
        singleMeeting['mid']=meeting.meeting_id
        singleMeeting['mtitle']=meeting.meeting_title
        singleMeeting['mtype']=meeting.meeting_type
        singleMeeting['mstart']=meeting.start_time.strftime( '%Y/%m/%d %H:%M' )
        singleMeeting['mperiod']=meeting.meeting_period
        singleMeeting['mclose']=meeting.close_time.strftime( '%Y/%m/%d %H:%M' )
        singleMeeting['mplace']=meeting.meeting_place
        singleMeeting['mtel']=meeting.contact_tel
        singleMeeting['memail']=str(meeting.contact_email)
        singleMeeting['muser']=meeting.create_user
        singleMeeting['mcreate']=meeting.create_time.strftime( '%Y-%m-%d' )
        singleMeeting['mstatus']=meeting.meeting_status
        meetingResult.append(singleMeeting)
    return meetingResult


def getSingleMeetingInfo(singleMeetingObj):
    singleMeetingData=dict()
    singleMeetingData['mid']=singleMeetingObj.meeting_id
    singleMeetingData['mtitle']=singleMeetingObj.meeting_title
    singleMeetingData['mtype']=singleMeetingObj.meeting_type
    singleMeetingData['mstart']=singleMeetingObj.start_time.strftime( '%Y/%m/%d %H:%M' )
    singleMeetingData['mperiod']=singleMeetingObj.meeting_period
    singleMeetingData['mclose']=singleMeetingObj.close_time.strftime( '%Y/%m/%d %H:%M' )
    singleMeetingData['mplace']=singleMeetingObj.meeting_place
    singleMeetingData['mtel']=singleMeetingObj.contact_tel
    singleMeetingData['memail']=str(singleMeetingObj.contact_email)
    singleMeetingData["mdetail"]=singleMeetingObj.detail
    singleMeetingData['muser']=singleMeetingObj.create_user
    singleMeetingData['mcreate']=singleMeetingObj.create_time.strftime( '%Y-%m-%d' )
    singleMeetingData['mstatus']=singleMeetingObj.meeting_status
    
    return singleMeetingData

def getMeetingParticipant(roleSet):
    roleResult=[]
    
    for role in roleSet:
        roleInfo=dict()
        roleInfo["rid"]=role.rid
        roleInfo["name"]=role.name
        roleInfo["sex"]=role.sex
        roleResult.append(roleInfo)
    
    return roleResult

def getAllGroups():
    '''
    
    '''
    pass