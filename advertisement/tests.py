from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

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
        view = views.AdvertisementViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/advertisement/delete/<{test_ad.id}>/')
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_ad.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_advertisement_not_owner(self):
        test_ad = BaseAdvertisement.objects.create(Title='test-title', owner=self.test_user)
        view = views.AdvertisementViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/advertisement/delete/<{test_ad.id}>/')
        force_authenticate(request, user=Account.objects.create_user('test_user2', "test2@example.com", "123456"))
        response = view(request, id=test_ad.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_clothes_advertisement(self):
        test_ad = ClothAdvertisement.objects.create(Title='test-title', owner=self.test_user, cloth_type='pants')
        view = views.AdvertisementViewSet.as_view({'put': 'update'})
        request = self.factory.put(f'/advertisement/update/<{test_ad.id}>/',
                                   data={'Title': 'updated-title', 'cloth_type': 'hat',
                                         'resourcetype': 'ClothAdvertisement'})
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_ad.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual([response.data['Title'], response.data['cloth_type']], ['updated-title', 'hat'])

    def test_update_food_advertisement(self):
        test_ad = FoodAdvertisement.objects.create(Title='test-title', owner=self.test_user, Food_type='meat')
        view = views.AdvertisementViewSet.as_view({'put': 'update'})
        request = self.factory.put(f'/advertisement/update/<{test_ad.id}>/',
                                   data={'Title': 'updated-title', 'Food_type': 'vegetables',
                                         'resourcetype': 'FoodAdvertisement'})
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_ad.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual([response.data['Title'], response.data['Food_type']], ['updated-title', 'vegetables'])

    def test_update_animal_advertisement(self):
        test_ad = AnimalAdvertisement.objects.create(Title='test-title', owner=self.test_user, animal_breed='husky')
        view = views.AdvertisementViewSet.as_view({'put': 'update'})
        request = self.factory.put(f'/advertisement/update/<{test_ad.id}>/',
                                   data={'Title': 'updated-title', 'animal_breed': 'bulldog',
                                         'resourcetype': 'AnimalAdvertisement'})
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_ad.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual([response.data['Title'], response.data['animal_breed']], ['updated-title', 'bulldog'])

    def test_update_service_advertisement(self):
        test_ad = ServiceAdvertisement.objects.create(Title='test-title', owner=self.test_user, service_type='medical')
        view = views.AdvertisementViewSet.as_view({'put': 'update'})
        request = self.factory.put(f'/advertisement/update/<{test_ad.id}>/',
                                   data={'Title': 'updated-title', 'service_type': 'dentistry',
                                         'resourcetype': 'ServiceAdvertisement'})
        force_authenticate(request, user=self.test_user)
        response = view(request, id=test_ad.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual([response.data['Title'], response.data['service_type']], ['updated-title', 'dentistry'])

    def test_load_advertisement(self):
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        test_ad3 = ServiceAdvertisement.objects.create(Title='test-title', owner=self.test_user, service_type='medical')
        test_ad2 = AnimalAdvertisement.objects.create(Title='test-title', owner=self.test_user,animal_breed='cat')
        test_ad1 = ClothAdvertisement.objects.create(Title='test-title', owner=self.test_user, cloth_type='hat')
        test_ad4 = ClothAdvertisement.objects.create(Title='test-titlex', owner= test_user2, cloth_type='hat')
        baseID = {test_ad1.id , test_ad2.id , test_ad3.id,test_ad4.id}
        view = views.LoadViewSet.as_view({'get': 'list'})
        request = self.factory.get('/advertisement/load-all/')
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        for ad in response.data : 
            self.assertEqual(ad['owner'], self.test_user.id)
            if ad['id'] not in baseID: 
                return AssertionError.__context__
            



