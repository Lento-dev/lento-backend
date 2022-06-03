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
