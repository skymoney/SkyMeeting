#-*-coding:utf-8-*-
'''
Created on 2013-4-9

@author: cheng
'''
from MemManage.models import *
from Meeting.models import *

def getTagList(t_list):
    tagList=[]
    for tag in t_list:
        singleTag={}
        singleTag["tid"]=tag.tid
        singleTag["tname"]=tag.tname
        singleTag["cid"]=tag.company_id
        tagList.append(singleTag)
    return tagList

def getGroupList(g_list):
    groupList=[]
    for g in g_list:
        singleGroup={}        
        singleGroup["gid"]=g.gid
        singleGroup["gname"]=g.gname
        singleGroup["cid"]=g.company_id
        groupList.append(singleGroup)
    return groupList