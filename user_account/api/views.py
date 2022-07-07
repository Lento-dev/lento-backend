import email
from typing_extensions import Required
from urllib import response
from rest_framework import generics, status, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from user_account.api.serializers import UserProfileSerializer 
from django.shortcuts import render, get_object_or_404
from user_account.permissions import Authorauthenticatedorhasaccess 
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from user_account.utils import Util
from user_account.api.serializers import UserProfileSerializer, PublicProfileSerializer , PublicProfileSerializerwithoutphonenumber
from user_account.models import Account
from django.core.exceptions import ValidationError

class UserProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    queryset = Account.objects.all()

    def get_object(self):
        return Account.objects.get(id=self.request.user.id)



@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def Access_phone_number(request):
    account = get_object_or_404(Account ,id = request.user.id)
    Access = request.POST.get('Phone_Access')
    response = {}
    print('status',Access)
    if(Access == 'true'): 
        account.access_phone = True  
        print('here')
        response['status'] = 'access to phone number is true'
    else: 
        account.access_phone = False
        response['status'] = 'access to phone number is false'
    account.save()

    return Response(response ,  status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def Access_profile(request):
    account = get_object_or_404(Account ,id = request.user.id)
    Access = request.POST.get('Profile_Access')
    response = {}
    if(Access == 'true'):
        account.access_profile = True  
        response['status'] = 'access to profile is true'
    else: 
        account.access_profile = False
        response['status'] = 'access to profile is false'
    account.save()
    print(account.access_profile)
    return Response(response ,  status=status.HTTP_200_OK)


       

	
class PublicUserProfileView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated ,Authorauthenticatedorhasaccess ]
    queryset = Account.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        user = Account.objects.get(id = self.kwargs[self.lookup_field]) 
        if user.access_phone:
            return PublicProfileSerializer
        else: 
            return PublicProfileSerializerwithoutphonenumber
        


@api_view(['GET', ]) 
@permission_classes([IsAuthenticated, ])
def verification(request):
    data = {}
    try: 
        data['resonse'] =  'success'
        email=request.GET.get('email')
        current_site = '' 
        absurl='http://' + current_site + "?email=" + email  
        email_body = 'use link below to verify your email\n' + 'domain:' + absurl
        data = {'content':email_body ,'subject':'please verify you email' ,'to_email':[email]}	
        print('*' * 50)
        Util.send_email(data)	
        
        return Response(data)

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})





#activating user account
@api_view(['GET', ]) 
@permission_classes([IsAuthenticated, ])
def changeEmail( request):
	
	NewEmail=request.GET.get('email')
	user = request.user
	user.email = NewEmail
	user.save()
	return Response('New Email is successfully confirmed') 