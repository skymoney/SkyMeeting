from Login.models import Account  
   
class MyCustomBackend:  
  
	def authenticate(self, username=None, password=None):  
		try:  
			user = Account.objects.get(aname = username)  
		except Account.DoesNotExist:  
			return None
		if user.check_password(password):  
			return user  
		else:
			return None  
   
   
	def get_user(self, user_id):  
		try:  
			return Account.objects.get(pk=user_id)  
		except Account.DoesNotExist:  
			return None  