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