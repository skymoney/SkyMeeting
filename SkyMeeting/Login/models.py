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
							  last_login=now, date_joined=now)

			account.set_password(password)
			account.save(using=self._db)
			return account

# Create your models here.

class Account(models.Model):  
	aname = models.CharField(max_length=50) 
	apassword=models.CharField(max_length=50)
	last_login=models.DateTimeField()        #create time
	date_joined=models.DateTimeField()   #last login time
	alevel=models.CharField(max_length=20)
	
	objects = AccountManager()
  
	def is_authenticated(self):  
		return True  
  
	def hashed_password(self, password=None):  
		if not password:  
			return self.apassword  
		else:  
			return hashlib.md5(password).hexdigest()  
          
	def check_password(self, password):  
		if self.hashed_password(password) == self.apassword:  
			return True  
		return False  
		
	def set_password(self, raw_password):
		self.apassword = self.hashed_password(raw_password)
      
	class Meta:  
		db_table = "Account"  