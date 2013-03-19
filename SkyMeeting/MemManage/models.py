from django.db import models

# Create your models here.
from Login.models import Account


class Company(models.Model):
    cname=models.CharField(max_length=100)
    clocation=models.CharField(max_length=100)

class Group(models.Model):
    gname=models.CharField(max_length=50)
    cid=models.ForeignKey(Company)

class Tag(models.Model):
    tname=models.CharField(max_length=50)
    cid=models.ForeignKey(Company)

#in fact this is role for company
class User(models.Model):
    name=models.CharField(max_length=30)
    sex=models.CharField(max_length=5)
    location=models.CharField(max_length=50)
    idcard=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    cid=models.ForeignKey(Company)
    aid=models.ForeignKey(Account)
    groups=models.ManyToManyField(Group)
    tags=models.ManyToManyField(Tag)