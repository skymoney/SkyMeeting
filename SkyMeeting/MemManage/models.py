#-*-coding:utf-8-*-
'''
Created on 2013-3-28

@author: cheng
'''
from django.db import models
import simplejson as json

from Login.models import Account

class Company(models.Model):
    #Company table
    cid=models.AutoField(primary_key=True,db_column="company_id")       #primary key of Company table
    cname=models.CharField(max_length=100,db_column="company_name")     #Company name of Company table
    clocation=models.CharField(max_length=100,db_column="company_location") #location of Company table
    
    class Meta:
        db_table="Company"      #set table name as Company



class GroupManager(models.Manager):
    '''
    group manager to convert
    Group list to string
    '''
    def getAllString(self):
        result=[]
        for group in self.all():
            group_dict=dict()
            group_dict["gid"]=group.id
            group_dict["gname"]=group.gname
            group_dict["cid"]=group.cid.id
            result.append(group_dict)
        return json.dumps(result)

class Group(models.Model):
    #Group table
    gid=models.AutoField(primary_key=True,db_column="group_id")     #primary key of Group table
    gname=models.CharField(max_length=50,db_column="group_name")    #name of Group table 
    company=models.ForeignKey(Company,db_column="group_company")      #company as foreign key
    
    objects=GroupManager()      #customize manager
    def toString(self):         #convert Group obj to string
        return "{'gid':"+str(self.gid)+",'gname':"+self.gname+",'cid':"+str(self.cid)+"}"
    
    def __unicode__(self):      #default __unicode__ method
        return self.gname
    
    class Meta:
        db_table="Group"



class TagManager(models.Manager):
    '''
    tag manager of Tag table
    to convert Tag list to String
    '''
    def getAllString(self):
        result=[]
        for tag in self.all():
            tag_dict=dict()
            tag_dict["tid"]=tag.id
            tag_dict["tname"]=tag.tname
            tag_dict["cid"]=tag.cid_id
            result.append(tag_dict)
        return json.dumps(result)

class Tag(models.Model):
    #Tag table
    tid=models.AutoField(primary_key=True,db_column="tag_id")       #tag id of Tag table
    tname=models.CharField(max_length=50,db_column="tag_name")      #name of Tag table
    company=models.ForeignKey(Company,db_column="tag_company")      #company as foreign key of Tag
    
    objects=TagManager()    #customize manager of Tag
    def toString(self):     #convert Tag obj to String
        return "{'tid':"+str(self.id)+",'tname':"+self.tname+",'cid':"+str(self.cid.id)+"}"
    
    def __unicode__(self):  #default __unicode__ method
        return self.tname
    
    class Meta:
        db_table="Tag"

class Role(models.Model):
    #Role table
    rid=models.AutoField(primary_key=True,db_column="role_id")      #id of Role table
    name=models.CharField(max_length=30,db_column="role_name")      #name of Role
    sex=models.IntegerField(default=-1,db_column="role_sex")        #sex of Role
    location=models.CharField(max_length=50,db_column="role_location")  #location of Role
    idcard=models.CharField(max_length=20,db_column="role_idcard")  #idcard of Role
    phone=models.CharField(max_length=15,db_column="role_phone")    #phone of Role
    email=models.EmailField(max_length=30,db_column="role_email")   #email of Role
    account=models.ForeignKey(Account,db_column="role_account")     #account as Foreign key of Role
    company=models.ForeignKey(Company,db_column="role_company")                              #company as Foreign key of Role
    groups=models.ManyToManyField(Group)                            #Group as many-to-many of Role
    tags=models.ManyToManyField(Tag)                                #Tag as many-to-many of Role
    
    class Meta:
        db_table="Role"

class TempRole(models.Model):
    #TempRole table
    trid=models.AutoField(primary_key=True,db_column='TempRoleId')
    name=models.CharField(max_length=30,db_column='TempRoleName')
    idcard=models.CharField(max_length=20,db_column='TempRoleIdCard')
    phone=models.CharField(max_length=15,db_column='TempRolePhone')
    email=models.CharField(max_length=30,db_column='TempRoleEmail')
    company=models.ForeignKey(Company,db_column='TempRoleCompany')
    
    code=models.CharField(max_length=50,default="",db_column='TempCheckCode')
    
    verifyByName=models.IntegerField(default=0,db_column='VerifyModeName')
    verifyByPhone=models.IntegerField(default=0,db_column='VerifyModePhone')
    verifyByQuest=models.IntegerField(default=0,db_column='VerifyModeQuest')
    verifyQuest=models.CharField(max_length=100,default="",db_column='VerifyQuest')
    verifyAnswer=models.CharField(max_length=100,default="",db_column='VerifyAnswer')
    
    class Meta:
        db_table='TempRole'
