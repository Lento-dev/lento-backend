from operator import truediv
from rest_framework import serializers
from user_account.models import Account
from django.core.serializers.json import DjangoJSONEncoder 
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import os

#sign_up 
class RegistrationSerializer(serializers.ModelSerializer):

	password2 	= serializers.CharField(style={'input_type': 'password'}, write_only=True)
	# writer 	= serializers.CharField()
	class Meta:
		model = Account
		fields = ['firstname' , 'lastname','email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}


	def	save(self,  *args, **kwargs):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)

		account.firstname = self.validated_data['firstname'] 
		account.lastname = self.validated_data['lastname']
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
       #hello
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		#account.is_active=True
		account.save()
		# account.create(self.validated_data)
    
		return account

        


