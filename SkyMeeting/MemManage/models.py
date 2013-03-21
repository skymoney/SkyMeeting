from django.db import models

# Create your models here.
from Login.models import Account


class Company(models.Model):
    cname=models.CharField(max_length=100)
    clocation=models.CharField(max_length=100)

class Group(models.Model):
    gname=models.CharField(max_length=50)
    cid=models.ForeignKey(Company)
    
    def toString(self):
        return "{'gid':"+str(self.id)+",'gname':"+self.gname+",'cid':"+str(self.cid)+"}"
    
    def __unicode__(self):
        return self.gname

class Tag(models.Model):
    tname=models.CharField(max_length=50)
    cid=models.ForeignKey(Company)
    
    def toString(self):
        return "{'tid':"+str(self.id)+",'tname':"+self.tname+",'cid':"+str(self.cid)+"}"
    
    def __unicode__(self):
        return self.tname

#in fact this is role for company
class Role(models.Model):
    name=models.CharField(max_length=30)
    sex=models.CharField(max_length=5)
    location=models.CharField(max_length=50)
    idcard=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    aid=models.ForeignKey(Account)
    company=models.ForeignKey(Company)
    groups=models.ManyToManyField(Group)
    tags=models.ManyToManyField(Tag)