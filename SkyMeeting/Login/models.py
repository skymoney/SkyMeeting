from django.db import models
from django.utils import timezone
import hashlib

class AccountManager(models.Manager):
    def create_user(self, username,  password=None):
            """
            Creates and saves a User with the given username, email and password.
            """
            now = timezone.now()
            if not username:
                raise ValueError('The given username must be set')
            account = self.model(aname=username,
                              last_login=now, date_joined=now,alevel="0")

            account.set_password(password)
            account.save(using=self._db)
            return account

# Create your models here.

class Account(models.Model):
    aid=models.AutoField(primary_key=True,db_column="account_id")
    aname = models.CharField(max_length=50,db_column="account_name") 
    apassword=models.CharField(max_length=50,db_column="account_password")
    last_login=models.DateTimeField(db_column="account_createtime")        #create time
    date_joined=models.DateTimeField(db_column="account_lastlogin")   #last login time
    alevel=models.CharField(max_length=20,db_column="account_level")  #should change CharField to Int
    
    objects = AccountManager()
  
    def is_authenticated(self):  
        return True 
          
    def check_password(self, password):  
        if password == self.apassword:  
            return True  
        return False  
        
    def set_password(self, raw_password):
        self.apassword = raw_password
      
    class Meta:  
        db_table = "Account"  
        
class TempAccountPwd(models.Model):
    #store temp account code to find password
    tapid=models.AutoField(primary_key=True,db_column="tmp_accountpwd_id")
    tapCode=models.CharField(max_length=50,db_column="tmp_accountpwd_code")
    tapAid=models.ForeignKey(Account,db_column="tmp_accountpwd_account")
    tapDate=models.DateTimeField(db_column="tmp_accountpwd_time")
    
    class Meta:
        db_table="TempAccountPwd"