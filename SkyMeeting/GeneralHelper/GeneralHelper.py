'''
Created on 2013-4-17

@author: cheng
'''
from Meeting.models import *
from MemManage.models import *

def getDashboard(account):
    '''
    get all info given one specified account
    @param account: account obj
    '''
    #corresponding roles of account,at least one
    dashInfoSet=[]
    
    role_set=account.role_set.all()
    for role in role_set:
        dashInfoSingle=dict()
        dashInfoSingle["companyName"]=role.company.cname
        dashInfoSingle["companyAdmin"]=role.company.role_set.filter(account_id=1)[0].name
        dashInfoSingle["membersCount"]=len(role.company.role_set.all())
        meeting_set=Meeting.objects.filter(meeting_participant__role_id=role.rid)
                
        dashInfoSingle["allMeetingsCount"]=len(meeting_set)
        dashInfoSingle["activeMeetingsCount"]=len(meeting_set.filter(meeting_status__lt=10))
        dashInfoSingle["closedMeetingsCount"]=len(meeting_set.filter(meeting_status=15))
        
        if len(meeting_set)>0:
            lastMeeting=meeting_set.order_by("start_time")[0]
            last=lastMeeting.meeting_title+" "+str(lastMeeting.start_time)
        else:
            last=""
        dashInfoSingle["lastmeeting"]=last
        dashInfoSet.append(dashInfoSingle)
    
    return dashInfoSet


def getProfile(params):
    '''
    get personal profile given specified id
    @param rid: role id
    '''    
    role=Role.objects.get(rid=params["rid"])
    profileInfo=dict()
    profileInfo["name"]=role.name
    profileInfo["sex"]=role.sex
    profileInfo["idcard"]=role.idcard
    profileInfo["phone"]=role.phone
    profileInfo["email"]=role.email
    
    return profileInfo