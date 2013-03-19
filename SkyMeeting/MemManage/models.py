from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=30)
    sex=models.CharField(max_length=5)
    location=models.CharField(max_length=50)
    idcard=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)

class Company(models.Model):
    cname=models.CharField(max_length=40)
    

class Group(models.Model):
    gname=models.CharField(max_length=30)

class Tag(models.Model):
    tname=models.CharField(max_length=30)

