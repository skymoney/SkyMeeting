from django.db import models
import simplejson as json

# Create your models here.
from Login.models import Account


class Company(models.Model):
    cname=models.CharField(max_length=100)
    clocation=models.CharField(max_length=100)

class GroupManager(models.Manager):
    def getAllString(self):
        result=[]
        for group in self.all():
            group_dict=dict()
            group_dict["gid"]=group.id
            group_dict["gname"]=group.tname
            group_dict["cid"]=group.cid.id
            result.append(group_dict)
        return json.dumps(result)

class Group(models.Model):
    gname=models.CharField(max_length=50)
    cid=models.ForeignKey(Company)
    
    objects=GroupManager()
    def toString(self):
        return "{'gid':"+str(self.id)+",'gname':"+self.gname+",'cid':"+str(self.cid)+"}"
    
    def __unicode__(self):
        return self.gname

class TagManager(models.Manager):
    def getAllString(self,kword):
        result=[]
        for tag in self.filter(cid=kword):
            tag_dict=dict()
            tag_dict["tid"]=tag.id
            tag_dict["tname"]=tag.tname
            tag_dict["cid"]=tag.cid.id
            result.append(tag_dict)
        return json.dumps(result)

class Tag(models.Model):
    tname=models.CharField(max_length=50)
    cid=models.ForeignKey(Company)
    
    objects=TagManager()
    def toString(self):
        return "{'tid':"+str(self.id)+",'tname':"+self.tname+",'cid':"+str(self.cid.id)+"}"
    
    def __unicode__(self):
        return self.tname

#in fact this is role for company
class Role(models.Model):
    name=models.CharField(max_length=30)
    sex=models.IntegerField(default=-1)
    location=models.CharField(max_length=50)
    idcard=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    aid=models.ForeignKey(Account)
    company=models.ForeignKey(Company)
    groups=models.ManyToManyField(Group)
    tags=models.ManyToManyField(Tag)