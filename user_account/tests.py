from tkinter.tix import Tree
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from .models import Account
from .api import views


class UserAccountViewsTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_user = Account.objects.create_user('test_user', "test@example.com", "123456")

    def test_get_user_profile_unauthorized(self):
        view = views.UserProfileRetrieveUpdateView.as_view({'get': 'retrieve'})
        request = self.factory.get('/api/account/user-profile/')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_profile(self):
        view = views.UserProfileRetrieveUpdateView.as_view({'get': 'retrieve'})
        request = self.factory.get('/api/account/user-profile/')
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_profile_unauthorized(self):
        view = views.UserProfileRetrieveUpdateView.as_view({'put': 'update'})
        request = self.factory.put('/api/account/edit-profile/')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_user_profile(self):
        view = views.UserProfileRetrieveUpdateView.as_view({'put': 'update'})
        request = self.factory.put('/api/account/edit-profile/', data={'first_name': 'test'})
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'test')

    def test_update_user_email(self):
        view = views.UserProfileRetrieveUpdateView.as_view({'put': 'update'})
        request = self.factory.put('/api/account/edit-profile/', data={'email': 'test@email.com'})
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@email.com')

    def test_public_profile(self):
        test_user = Account.objects.create_user('test_user2', "test2@example.com", "123456")
        view = views.PublicUserProfileView.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/api/account/public-profile/{test_user.id}/')
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'test_user2')

    def test_access_profile_api(self):
        view = views.Access_profile
        request = self.factory.post('/api/account/access-profile/',
                                    data={'Profile_Access': 'true'})
        
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'] ,'access to profile is true' )


    def test_access_profile_api_2(self):

        view = views.Access_profile
        request = self.factory.post('/api/account/access-profile/',
                                    data={'Profile_Access': 'false'})
        
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'access to profile is false')



    def test_access_phone_api(self):
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "123456")
        view = views.Access_phone_number
        request = self.factory.post('/api/account/access-phone/',
                                    data={'Phone_Access': 'true'})
        
        force_authenticate(request, user=test_user2)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'] , 'access to phone number is true')


    def test_access_phone_api_2(self):
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "123456")
        
        view = views.Access_phone_number
        request = self.factory.post('/api/account/access-phone/',
                                    data={'Phone_Access': 'false'})
        
        force_authenticate(request, user=test_user2)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'] , 'access to phone number is false')


    def test_public_profile_access(self):
        test_user = Account.objects.create_user('test_user2', "test2@example.com", "123456")
        test_user.access_profile = False
        test_user.save() 
        view = views.PublicUserProfileView.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/api/account/public-profile/{test_user.id}/')
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_user.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_public_profile_access_true(self):
        test_user = Account.objects.create_user('test_user2', "test2@example.com", "123456")
        test_user.access_profile = True
        test_user.save() 
        view = views.PublicUserProfileView.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/api/account/public-profile/{test_user.id}/')
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


     

    
        




    


    
