from django.db import models

# Create your models here.
class Account(models.Model):
    aid=models.AutoField(primary_key=True,db_column="account_id")
    aname=models.CharField(max_length=50,db_column="account_name")
    apassword=models.CharField(max_length=50,db_column="account_password")
    atime=models.DateTimeField(db_column="account_createtime")        #create time
    alastlogin=models.DateTimeField(db_column="account_lastlogin")   #last login time
    
    class Meta:
        db_table="Account"