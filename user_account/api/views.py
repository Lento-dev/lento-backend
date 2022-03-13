
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
from django.views import generic
from rest_framework import status 
from rest_framework import generics
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from user_account.api.serializers import RegistrationSerializer
from django.core import validators
from django.core.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder 
from django.contrib.auth import logout , login
from rest_framework.views import APIView
from user_account.models import Account
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from . import urls
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate

@api_view(['POST', ]) 
@permission_classes([])
@authentication_classes([])  
def registration_view(request):
	try: 
		if request.method == 'POST':
			serializer = RegistrationSerializer(data=request.data)
			data = {}
			if serializer.is_valid():
               
				account = serializer.save()
                #have to change 
				data['response'] = 'successfully registered new user'
				data['email'] = account.email
				data['username'] = account.username
				data['firstname'] = account.firstname
				data['lastname'] = account.lastname
				token = Token.objects.get(user=account).key
				data['token'] = token
				#send_email_content(token , request , account)
                
			else:
				data = serializer.errors

			return Response(data)

	except KeyError as e:
		print(e)
		raise ValidationError({"400": f'Field {str(e)} missing'})


def validate_email(email):
	account = None
	try:
		account = Account.objects.get(email=email)
	except Account.DoesNotExist:
		return None
	if account != None:
		return email

def validate_username(username):
	account = None
	try:
		account = Account.objects.get(username=username)
	except Account.DoesNotExist:
		return None
	if account != None:
		return username

#login class

class ObtainAuthTokenView(APIView):

	authentication_classes = []
	permission_classes = []
	
	def post(self, request):
		context = {}
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		account = authenticate(username=username, password=password)
		#print("fortest" ,account.email == email)
		if (account):
			try:
				
				token = Token.objects.get(user=account)
               
			except Token.DoesNotExist:
				token = Token.objects.create(user=account)
			if(account.is_active):
                #print("this os")
				context['response'] = 'Successfully authenticated.'
				context['pk'] = account.pk
				context['username'] = username.lower()
				context['token'] = token.key
              
			else: 
				context['error_message'] = 'Invalid credentials for emails'
				return Response( " this is Invalid credentials",status=status.HTTP_400_BAD_REQUEST) 
			
		else:
			context['response'] = 'Error'
			context['error_message'] = 'Invalid credentials'
			return Response( "ERROR !Invalid credentials",status=status.HTTP_400_BAD_REQUEST) 
	 

		return Response(context)

#existence of an account 
@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def does_account_exist_view(request):

	if request.method == 'GET':
		email = request.GET['email'].lower()
		data = {}
		try:
			account = Account.objects.get(usernme=email)
			data['response'] = email
		except Account.DoesNotExist:
			data['response'] = "Account does not exist"
		return Response(data)

#Delete account 
class DeleteAccount(APIView):
	
	permission_classes = [IsAuthenticated]

	def delete(self, request, *args, **kwargs):
		user=self.request.user
		user.delete()

		return Response({"result":"user is deleted"})



#loging out user 
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):

	request.user.auth_token.delete()
	logout(request)
	return Response('User Logged out successfully')
	