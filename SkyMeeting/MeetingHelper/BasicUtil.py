'''
Created on 2013-4-8

@author: cheng
'''

def query2List(meetingData):
    meetingResult=[]
    
    for meeting in meetingData:
        singleMeeting=dict()
        singleMeeting['mid']=meeting.meeting_id
        singleMeeting['mtitle']=meeting.meeting_title
        singleMeeting['mtype']=meeting.meeting_type
        singleMeeting['mstart']=str(meeting.start_time)
        singleMeeting['mperiod']=meeting.meeting_period
        singleMeeting['mclose']=str(meeting.close_time)
        singleMeeting['mplace']=meeting.meeting_place
        singleMeeting['mtel']=meeting.contact_tel
        singleMeeting['memail']=str(meeting.contact_email)
        singleMeeting['mdetail']=meeting.detail
        singleMeeting['muser']=meeting.create_user
        singleMeeting['mcreate']=str(meeting.create_time)
        
        meetingResult.append(singleMeeting)
    return meetingResult