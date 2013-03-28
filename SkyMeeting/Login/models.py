from django.db import models
import hashlib

# Create your models here.

class Account(models.Model):  
	aname = models.CharField(max_length=50) 
	apassword=models.CharField(max_length=50)
	last_login=models.DateTimeField()        #create time
	date_joined=models.DateTimeField()   #last login time
	alevel=models.CharField(max_length=20)
  
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
      
	class Meta:  
		db_table = "Account"  