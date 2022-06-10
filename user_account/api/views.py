from typing_extensions import Required
from urllib import response
from rest_framework import generics, status, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from user_account.api.serializers import UserProfileSerializer 
from django.shortcuts import render, get_object_or_404
from user_account.permissions import Authorauthenticatedorhasaccess 


from user_account.api.serializers import UserProfileSerializer, PublicProfileSerializer , PublicProfileSerializerwithoutphonenumber
from user_account.models import Account


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
        response['status'] = 'access to phone number is true'
    else: 
        account.access_phone = False
        response['status'] = 'access to phone number is false'
    account.save()

    return Response(response ,  status=status.HTTP_201_CREATED)


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

    return Response(response ,  status=status.HTTP_201_CREATED)


       


	
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
        


