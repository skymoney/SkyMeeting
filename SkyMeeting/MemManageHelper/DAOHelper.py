'''
Created on 2013-3-23

@author: cheng
'''
from MemManage.models import Role,Tag,Group,Company,TempRole
import simplejson as json
import BasicUtil as util

def member(request):
    u_list=Role.objects.filter(company_id=1).distinct()
    RoleCount=len(u_list)
    #def conf variable to store current 
    #groups and tags info
    returnDict=dict()
    
    conf={}
    conf["current_gid"]=-1
    conf["current_tid"]=-1
        
    if 'gid' in request.GET and len(request.GET['gid'])>0:
        if request.GET['gid']=="-1":
            pass
        else:
            try:
                u_list=u_list.filter(groups__id=int(request.GET['gid'])).distinct()
                conf['current_gid']=int(request.GET['gid'])
            except:
                pass
    if 'tid' in request.GET and len(request.GET['tid'])>0:
        if '-1' in request.GET['tid'].split():
            pass
        else:
            try:
                u_list=u_list.filter(tags__id__in=(request.GET['tid'].split())).distinct()
                print u_list
                conf['current_tid']=util.listToInt(request.GET['tid'].split())
            except:
                pass
       
    g_list=Group.objects.filter(cid=1)
    t_list=Tag.objects.filter(cid=1)
    groupList=[]
    tagList=[]
    for tag in t_list:
        singleTag={}
        singleTag["tid"]=tag.id
        singleTag["tname"]=tag.tname
        singleTag["cid"]=tag.cid_id
        tagList.append(singleTag)
    #here can optimize by just sql query instead of Model method
    for g in g_list:
        singleGroup={}
        num=len(Role.objects.filter(company_id=1,groups__id=g.id))
        singleGroup["gid"]=g.id
        singleGroup["gname"]=g.gname
        singleGroup["cid"]=g.cid_id
        singleGroup["count"]=num
        groupList.append(singleGroup)
    #conf can set more values here
    #return data
    returnDict["memberAll"]=u_list
    returnDict["groupAll"]=groupList
    returnDict["groupString"]=json.dumps(groupList)
    returnDict["groupAllCount"]=RoleCount    
    returnDict["tagAll"]=t_list
    returnDict["tagString"]=json.dumps(tagList)
    returnDict["conf"]=conf
    
    return returnDict

def editRoleInfo(request):
    result=dict()
    try:
        roleid=int(request.POST["id"])
        Role.objects.filter(id=roleid).update(
                     name=request.POST["name"],
                     sex=int(request.POST["sex"]),
                     idcard=request.POST["idcard"],
                     phone=request.POST["phone"],
                     email=request.POST["email"])
        #clear all original groups and tags
        Role.objects.get(id=roleid).groups.clear()
        Role.objects.get(id=roleid).tags.clear()
        
        #here can be optimized by sql query instead of model method
        if len(request.POST["groupIds"])>0:
            groupIds=request.POST["groupIds"].split('+')
            for group in groupIds:
                Role.objects.get(id=roleid).groups.add(int(group))
        if len(request.POST['tagIds'])>0:
            tagIds=request.POST["tagIds"].split('+')
            for tag in tagIds:
                Role.objects.get(id=roleid).tags.add(int(tag))
        result["success"]="true"
    except:
        result["success"]="false"
        result["errorcode"]=""  #add error status
        result["error"]=""
    return result

def addGroup(request):
    #add new group
    gname=request.POST['groupName']
    #here add permission deal
    ng=Group()
    ng.gname=gname
    ng.cid=Company.objects.get(id=1)
    result=dict()
    try:
        ng.save()
        ng_id=ng.id
        result["success"]="true"
        result["gid"]=ng_id
    except:
        result["success"]="false"
        result["error"]=""  #describe error status
        result["errorcode"]=""
    return result

def addTag(request):
    #add new tag
    tname=request.POST["tagName"]
    nt=Tag()
    nt.tname=tname
    nt.cid=Company.objects.get(id=1)
    result=dict()
    try:
        nt.save()
        nt_id=nt.id
        result["success"]="true"
        result["tid"]=nt_id
    except:
        result["success"]="fasle"
        result["error"]=""  #descript error status
        result["errorcode"]=""
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
            
            #call send email func to send email
            result["success"]="true"
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
        Role.objects.filter(id=rid).delete()
        result["success"]="true"
    except:
        result["success"]="false"
        result["errors"]=""
    return result

def deleteTag(params):
    cid=params["cid"]
    tid=params["tid"]
    result=dict()
    try:
        Tag.objects.filter(id=tid).delete()
        result["success"]="true"
    except:
        result["succss"]="false"
        result["errors"]=""
    return result