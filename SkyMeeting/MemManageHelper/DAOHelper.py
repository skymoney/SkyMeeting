#-*- coding:utf-8 -*-
'''
Created on 2013-3-23

@author: cheng
'''
from MemManage.models import Role,Tag,Group,Company,TempRole
import simplejson as json
import BasicUtil as util
from GlobalUtil import DataUtil,RequestUtil
def members(params):
    '''
    get members given conditions
    @param gid: company id
    @param gid: group id
    @param tid: tag id
    @param pn: page number   
    default order by name, 10 persons once
    '''
    u_list=Role.objects.filter(company_id=params['cid']).distinct()
    RoleCount=len(u_list)
    #def conf variable to store current 
    #groups and tags info
    returnDict=dict()
    
    conf={}
    conf["current_gid"]=-1
    conf["current_tid"]=-1
        
    if 'gid' in params and len(params['gid'])>0:
        if params['gid']=="-1":
            pass
        else:
            try:
                u_list=u_list.filter(groups__gid=int(params['gid'])).distinct()
                conf['current_gid']=int(params['gid'])
            except:
                pass
    if 'tid' in params and len(params['tid'])>0:
        if '-1' in params['tid'].split():
            pass
        else:
            try:
                u_list=u_list.filter(tags__tid__in=(params['tid'].split())).distinct()
                print u_list
                conf['current_tid']=util.listToInt(params['tid'].split())
            except:
                pass
    
    #add paging
    #pageResult=RequestUtil.pagingOps(u_list,'rid',params["pn"])
    from django.core.paginator import Paginator
    from django.conf import settings
    
    pageData=Paginator(u_list,settings.NUMBERPERPAGE)
    g_list=Group.objects.filter(company=params["cid"])
    t_list=Tag.objects.filter(company=params["cid"])
    
    tagList=DataUtil.getTagList(t_list)
    #here can optimize by just sql query instead of Model method
    groupList=DataUtil.getGroupList(g_list)
    for group in groupList:
        num=len(Role.objects.filter(company_id=params["cid"],groups__gid=group["gid"]))
        group["count"]=num
        
    #conf can set more values here
    #return data
    returnDict["memberAll"]=pageData.page(int(params["pn"])).object_list
    returnDict["groupAll"]=groupList
    returnDict["groupString"]=json.dumps(groupList)
    returnDict["groupAllCount"]=RoleCount    
    returnDict["tagAll"]=t_list
    returnDict["tagString"]=json.dumps(tagList)
    returnDict["conf"]=conf
    returnDict["tpn"]=pageData.page_range
    returnDict["pn"]=int(params["pn"])
    
    return returnDict

def editRoleInfo(params):
    result=dict()
    try:
        roleid=int(params["id"])
        Role.objects.filter(rid=roleid).update(
                     name=params["name"],
                     sex=int(params["sex"]),
                     idcard=params["idcard"],
                     phone=params["phone"],
                     email=params["email"])
        #clear all original groups and tags
        Role.objects.get(rid=roleid).groups.clear()
        Role.objects.get(rid=roleid).tags.clear()
        
        #here can be optimized by sql query instead of model method
        if len(params["groupIds"])>0:
            groupIds=params["groupIds"].split('+')
            for group in groupIds:
                Role.objects.get(rid=roleid).groups.add(int(group))
        if len(params['tagIds'])>0:
            tagIds=params["tagIds"].split('+')
            for tag in tagIds:
                Role.objects.get(rid=roleid).tags.add(int(tag))
        result["success"]="true"
    except:
        result["success"]="false"
        result["errors"]=""
    return result

def addGroup(params):
    #add new group
    cid=params['cid']
    gname=params['groupName']
    #here add permission deal
    ng=Group()
    ng.gname=gname
    ng.company=Company.objects.get(cid=cid)
    result=dict()
    try:
        ng.save()
        ng_id=ng.gid
        result["success"]="true"
        result["gid"]=ng_id
    except:
        result["success"]="false"
        result["errors"]=""
    return result

def editGroup(params):
    #edit group name given group id
    cid=params["cid"]
    gid=params["gid"]
    newName=params["gname"]
    result=dict()
    try:
        Group.objects.filter(gid=gid).update(gname=newName)
        result["success"]="true"
    except:
        result["success"]="false"
        result["errors"]=""
    return result

def deleteGroup(params):
    #delete group given group id
    cid=params["cid"]       #verify and confirm delete info
    gid=params["gid"]
    result=dict()
    try:
        Group.objects.filter(gid=gid).delete()
        result["success"]="true"
    except:
        result["success"]="false"
        result["errors"]=""
    return result

def addTag(params):
    #add new tag
    cid=params["cid"]
    tname=params["tagName"]
    nt=Tag()
    nt.tname=tname
    nt.company=Company.objects.get(cid=cid)
    result=dict()
    try:
        nt.save()
        nt_id=nt.tid
        result["success"]="true"
        result["tid"]=nt_id
    except:
        result["succss"]="false"
        result["errors"]=""
    return result

def deleteTag(params):
    cid=params["cid"]
    tid=params["tid"]
    result=dict()
    try:
        Tag.objects.filter(tid=tid).delete()
        result["success"]="true"
    except:
        result["succss"]="false"
        result["errors"]=""
    return result

def inviteUser(params):
    #invite new user
    #here a temp table is needed to store info 
    #before user confirm and register
    
    #first verify whether exist in the table
    cid=params["cid"]
    idcard=params["idcard"]
    result=dict()
    try:
        if len(TempRole.objects.filter(idcard=params["idcard"],company_id=int(params["cid"])))>0:
            #already exist
            result["success"]="false"
            result["errors"]=""
            return result
        else:
            tr=TempRole()
            tr.name=params["name"]
            tr.idcard=params["idcard"]
            tr.phone=params["phone"]
            tr.email=params["email"]
            tr.company_id=int(params["cid"])
            tr.permission=int(params["authority"])
            from hashlib import md5
            import random
            randomcode=md5(str(int(random.uniform(0,1000)))).hexdigest()
            tr.code=randomcode
            verifyMode=params["verifyMode"]
            if len(verifyMode)>0:
                modeNumSet=util.listToInt(verifyMode.split('+'))
                for mode in modeNumSet:
                    if mode==1:
                        tr.verifyByName=1
                    if mode==2:
                        tr.verifyByPhone=1
                    if mode==9:
                        tr.verifyByQuest=1
                        tr.verifyQuest=params["verifyQuestion"]
                        tr.verifyAnswer=params["verifyAnswer"]
            else:
                pass
            
            tr.save()
            print params['email']
            #call send email func to send email
            if sendInviteEmail(params["email"],randomcode)==1:
                result["success"]="true"
                return result
            else:
                result['success']="false"
                result["errors"]=""
                return result
    except :
        result["success"]="false"
        result["errors"]=""
        return result

def deleteRole(params):
    #delete selected role
    rid=params["id"]
    #delete specified role!
    result=dict()
    #Attention this operation!!!!!!!
    try:
        Role.objects.filter(rid=rid).delete()
        result["success"]="true"
    except:
        result["success"]="false"
        result["errors"]=""
    return result

def queryPerson(params):
    '''
    query person given group id and company id
    10 persons once
    default order by name
    '''
    gid=params["gid"]
    cid=params["cid"]
    
    uList=Role.objects.filter(company_id=cid)
    if gid!="-1":
        uList=uList.filter(groups__gid=gid)
    
    #tids not in use currently
    if 'tid' in params and len(params['tid'])>0:
        if '-1' in params['tid'].split():
            pass
        else:
            try:
                uList=uList.filter(tags__tid__in=(params['tid'].split())).distinct()
            except:
                pass
    from django.core.paginator import Paginator
    from django.conf import settings
    #pageResult=RequestUtil.pagingOps(uList,'rid',params["pn"])
    pageData=Paginator(uList,settings.NUMBERPERPAGE)
    finalResult=dict()
    
    roleList=[]
    currentPageData=pageData.page(int(params["pn"])).object_list
    print currentPageData
    #get specified fields of Role
    for u in currentPageData:
        role=dict()
        role["id"]=u.rid
        role["name"]=u.name
        role["sex"]=u.sex
        roleList.append(role)
        
    finalResult["roleList"]=roleList
    finalResult["pn"]=int(params["pn"])
    finalResult["tpn"]=pageData.page_range
    return finalResult

def sendInviteEmail(email,code):
    from django.core.mail import send_mail
    subject="Invite You to Join US"
    content="http://192.168.100.21:8000/invite/?code="+code
    try:
        return_code=send_mail(subject,content,"CChain0615@gmail.com",[email],fail_silently=False)
        
        return return_code
    except:
        return_code=0
    return return_code
