from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from advertisement.api.serializers import Advertisement
from .models import BaseAdvertisement, ClothAdvertisement, ServiceAdvertisement, AnimalAdvertisement, FoodAdvertisement
from .api import views
from user_account.models import Account


class AdvertisementsTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_user = Account.objects.create_user('test_user', "test@example.com", "123456")

    def test_Add_ClothesAdvertisement(self):
        view = views.clothcreate.as_view({'post': 'create'})
        request = self.factory.post('/advertisement/addcloth/')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_Add_ClothesAdvertisement_user(self):
        view = views.clothcreate.as_view({'post': 'create'})
        request = self.factory.post('/advertisement/addcloth/',
                                    data={'Title': 'test', 'cloth_type': 'pants', 'for_men': True})
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['Title'], 'test')
        self.assertEqual(response.data['cloth_type'], 'pants')
        self.assertEqual(response.data['for_men'], True)

    def test_delete_advertisement(self):
        test_ad = BaseAdvertisement.objects.create(Title='test-title', owner=self.test_user)
        view = views.DeleteAdvertisementView.as_view()
        request = self.factory.delete(f'/advertisement/delete/<{test_ad.id}>/')
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_ad.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_advertisement_not_owner(self):
        test_ad = BaseAdvertisement.objects.create(Title='test-title', owner=self.test_user)
        view = views.DeleteAdvertisementView.as_view()
        request = self.factory.delete(f'/advertisement/delete/<{test_ad.id}>/')
        force_authenticate(request, user=Account.objects.create_user('test_user2', "test2@example.com", "123456"))
        response = view(request, id=test_ad.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
