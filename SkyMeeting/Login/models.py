from django.db import models

# Create your models here.
class Account(models.Model):
    aname=models.CharField(max_length=50)
    apassword=models.CharField(max_length=50)
    atime=models.DateTimeField()        #create time
    alastlogin=models.DateTimeField()   #last login time