from django import test
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from .filtersets import AdvertisementFilterSet
from .models import BaseAdvertisement, ClothAdvertisement, ServiceAdvertisement, AnimalAdvertisement, FoodAdvertisement , SavedModel , Comment
from .api import views
from user_account.models import Account
from django.utils.timezone import datetime



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

    
    def test_Add_ServiceAdvertisement_user(self):
        view = views.Servicecreate.as_view({'post': 'create'})
        request = self.factory.post('/advertisement/addservice/',
                                    data={'Title': 'test', 'service_type': 'medical'})
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['Title'], 'test')
        self.assertEqual(response.data['service_type'], 'medical')


    def test_Add_FoodAdvertisement_user(self):
        view = views.Foodcreate.as_view({'post': 'create'})
        request = self.factory.post('/advertisement/addfood/',
                                    data={'Title': 'test', 'Food_type': 'fastfood'})
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['Title'], 'test')
        self.assertEqual(response.data['Food_type'], 'fastfood')


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

    def test_filter_set(self):
        test_clothes_ad = ClothAdvertisement.objects.create(Title='test-cloth', owner=self.test_user,
                                                            expiration_date='2022-01-01')
        test_food_ad = FoodAdvertisement.objects.create(Title='test-food', owner=self.test_user,
                                                        expiration_date='2022-01-01')
        test_animal_ad = AnimalAdvertisement.objects.create(Title='test-animal', owner=self.test_user,
                                                            animal_breed='dog')
        test_service_ad = ServiceAdvertisement.objects.create(Title='test-service', owner=self.test_user,
                                                              expiration_date='2022-01-01')
        cloth_filter_set = AdvertisementFilterSet(data={'ad_type': 'ClothAdvertisement'},
                                                  queryset=BaseAdvertisement.objects.all())
        self.assertEqual(cloth_filter_set.qs.first().id, test_clothes_ad.id)
        food_filter_set = AdvertisementFilterSet(data={'ad_type': 'FoodAdvertisement'},
                                                 queryset=BaseAdvertisement.objects.all())
        self.assertEqual(food_filter_set.qs.first().id, test_food_ad.id)
        animal_filter_set = AdvertisementFilterSet(data={'ad_type': 'AnimalAdvertisement'},
                                                   queryset=BaseAdvertisement.objects.all())
        self.assertEqual(animal_filter_set.qs.first().id, test_animal_ad.id)
        service_filter_set = AdvertisementFilterSet(data={'ad_type': 'ServiceAdvertisement'},
                                                    queryset=BaseAdvertisement.objects.all())
        self.assertEqual(service_filter_set.qs.first().id, test_service_ad.id)
        clothes_expiration_date_filter_set = AdvertisementFilterSet(
            data={'clothadvertisement__expiration_date__gte': '2021-01-01'}, queryset=BaseAdvertisement.objects.all())
        self.assertEqual(clothes_expiration_date_filter_set.qs.first().id, test_clothes_ad.id)
        food_expiration_date_filter_set = AdvertisementFilterSet(
            data={'foodadvertisement__expiration_date__lte': '2022-01-02'}, queryset=BaseAdvertisement.objects.all())
        self.assertEqual(food_expiration_date_filter_set.qs.first().id, test_food_ad.id)
        service_expiration_date_filter_set = AdvertisementFilterSet(
            data={'serviceadvertisement__expiration_date__gte': '2021-01-01'},
            queryset=BaseAdvertisement.objects.all())
        self.assertEqual(service_expiration_date_filter_set.qs.first().id, test_service_ad.id)
        animal_breed_filter_set = AdvertisementFilterSet(data={'animaladvertisement__animal_breed': 'dog'},
                                                         queryset=BaseAdvertisement.objects.all())
        self.assertEqual(animal_breed_filter_set.qs.first().id, test_animal_ad.id)

    def test_search_advertisement_view(self):
        test_ad1 = ClothAdvertisement.objects.create(Title='test-cloth', owner=self.test_user)
        test_ad2 = FoodAdvertisement.objects.create(Title='test-food', owner=self.test_user)
        view = views.SearchAdvertisementView.as_view()
        request = self.factory.get('/advertisement/search/?search=cloth', {'search': 'cloth'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], test_ad1.id)

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

    def test_retrieve_advertisement(self):
        test_ad3 = ServiceAdvertisement.objects.create(Title='test-title', owner=self.test_user, service_type='medical')
        view = views.AdvertisementViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/advertisement/retrieve/<{test_ad3.id}>/')
        force_authenticate(request, user=self.test_user)
        response = view(request , id = test_ad3.id )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Title'] ,'test-title' )
        self.assertEqual(response.data['service_type'] ,'medical' )

    def test_sort_advertisement(self): 
        datetime1 = datetime(2015, 10, 11, 23, 55, 59, 342380)
        datetime2 = datetime(2013, 10, 10, 23, 55, 59, 342379)
        datetime3 = datetime(2020, 10, 12, 23, 55, 59, 342394)
      
        view = views.AdvertisementViewSetreturn.as_view({'get': 'list'})
        request = self.factory.get('/advertisement/homepageads/')
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        i = 0
        length = len(response.data)
        for ad in response.data : 
           if i < length -1:
               j = i+1
               if ad['date_joined'] < response.data[j]['date_joined']:
                    return AssertionError.__context__
               i += 1
               
    def test_save_advertisement(self): 
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1' )
        view = views.save_view2.as_view({'post': 'create'})
        request = self.factory.post('api/advertisement/Saves/' , data={'user_n': self.test_user.id, 'post_n': test_ad1.id})
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['save'], 'save')
        
    def test_unsave_advertisement(self): 
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1' )
        view = views.save_view2.as_view({'post': 'create'})
        savex = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad1)
        request = self.factory.post('api/advertisement/Saves/' , data={'user_n': self.test_user.id, 'post_n': test_ad1.id})
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['save'], 'unsave')
        
    def test_saveList_advertisement(self): 
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        test_ad2 = ServiceAdvertisement.objects.create(Title='test-title2', owner=self.test_user, service_type='medical2' )
        test_ad3 = AnimalAdvertisement.objects.create(Title='test-titlea3', owner=self.test_user, animal_breed='cat' )
        save1 = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad1)
        save2 = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad2)
        save3 = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad3)
        save4 = SavedModel.objects.create(user_n = test_user2, post_n =  test_ad3)
      
        view = views.save_view2.as_view({'get': 'list'})
        request = self.factory.get('api/advertisement/Savelist/')
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for save in response.data: 
            if save['user_n'] != self.test_user: 
                return AssertionError.__context__
            
    def test_saveList_advertisement_otheruser(self): 
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        test_ad2 = ServiceAdvertisement.objects.create(Title='test-title2', owner=self.test_user, service_type='medical2' )
        test_ad3 = AnimalAdvertisement.objects.create(Title='test-titlea3', owner=self.test_user, animal_breed='cat' )
        save1 = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad1)
        save2 = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad2)
        save3 = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad3)
      
        view = views.save_view2.as_view({'get': 'list'})
        request = self.factory.get('api/advertisement/Savelist/')
        force_authenticate(request, user=test_user2)
        response = view(request)
        self.assertEqual(len(response.data), 0)
        
            
    def test_save_retrieve_advertisement(self): 
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        save1 = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad1)
        view = views.save_view2.as_view({'get': 'retrieve'})
        request = self.factory.get(f'api/advertisement/Saves/<{save1.id}>/')
        force_authenticate(request, user=self.test_user)
        response = view(request , id = save1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['post_n'],  test_ad1.id)
        self.assertEqual(response.data['user_n'],  self.test_user.id)
        
    def test_save_retrieve_advertisement_forbidden(self): 
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        save1 = SavedModel.objects.create(user_n = self.test_user, post_n =  test_ad1)
        view = views.save_view2.as_view({'get': 'retrieve'})
        request = self.factory.get(f'api/advertisement/Saves/<{save1.id}>/')
        force_authenticate(request, user=test_user2)
        response = view(request , id = save1.id)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        
        
        
    def test_comment_create(self): 
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        view = views.CommentList.as_view()
        request = self.factory.post('api/advertisement/comment/' , data={'body': 'mycomment', 'post': test_ad1.id})
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['body'], 'mycomment')
        self.assertEqual(response.data['post'], test_ad1.id)
        
    def test_comment_lists(self): 
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        test_ad2 = ServiceAdvertisement.objects.create(Title='test-title2', owner=self.test_user, service_type='medical2' )
        test_ad3 = AnimalAdvertisement.objects.create(Title='test-titlea3', owner=self.test_user, animal_breed='cat' )
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        cm2 = Comment.objects.create(body = 'comment2' , post = test_ad2 , owner = self.test_user)
        cm3 = Comment.objects.create(body = 'comment3' , post = test_ad3 , owner = self.test_user)
        cm4 = Comment.objects.create(body = 'comment4' , post = test_ad3, owner = test_user2)
        dict = {cm1.id , cm2.id  , cm3.id , cm4.id}
        
        view = views.CommentList.as_view()
        request = self.factory.get('api/advertisement/comment/')
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        for cm in response.data: 
            if cm['id'] not in dict: 
                return AssertionError.__context__
                
    def test_comment_lists_of_post(self): 
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        test_ad2 = ServiceAdvertisement.objects.create(Title='test-title2', owner=self.test_user, service_type='medical2' )
        test_ad3 = AnimalAdvertisement.objects.create(Title='test-titlea3', owner=self.test_user, animal_breed='cat' )
        
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        cm2 = Comment.objects.create(body = 'comment2' , post = test_ad2 , owner = self.test_user)
        cm3 = Comment.objects.create(body = 'comment3' , post = test_ad3 , owner = self.test_user)
        cm4 = Comment.objects.create(body = 'comment4' , post = test_ad3, owner = test_user2)
        dict = {cm1.id , cm2.id  , cm3.id , cm4.id}
        
        view = views.Commentofpost.as_view()
        request = self.factory.get('api/advertisement/commenposts/')
        force_authenticate(request, user=self.test_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        for cm in response.data: 
            self.assertEqual(cm['owner'] , 'test_user')
            if cm['id'] not in dict: 
                return AssertionError.__context__
            
    def test_comment_retrieve(self): 
       
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        view = views.CommentDetail.as_view()
        request = self.factory.get(f'api/advertisement/comments/{cm1.id}/')
        force_authenticate(request, user=self.test_user)
        response = view(request ,  pk = cm1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], cm1.id)
        self.assertEqual(response.data['post'], test_ad1.id)
        self.assertEqual(response.data['owner']  , 'test_user')
        self.assertEqual(response.data['body']  , 'comment1')
        
    def test_comment_update_bad_Request(self): 
       
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        view = views.CommentDetail.as_view()
        request = self.factory.put(f'api/advertisement/comments/{cm1.id}/' , data={'body': 'newcomment' , 'post' : test_ad1.id})
        force_authenticate(request, user=self.test_user)
        response = view(request ,  pk = cm1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], cm1.id)
        self.assertEqual(response.data['post'], test_ad1.id)
        self.assertEqual(response.data['owner']  , 'test_user')
        self.assertEqual(response.data['body']  , 'newcomment')
        
        
    def test_comment_update(self): 
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        view = views.CommentDetail.as_view()
        request = self.factory.put(f'api/advertisement/comments/{cm1.id}/' , data={'body': 'newcomment' })
        force_authenticate(request, user=self.test_user)
        response = view(request ,  pk = cm1.id)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
        
    def test_comment_update_forbidden(self): 
       
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        view = views.CommentDetail.as_view()
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        request = self.factory.put(f'api/advertisement/comments/{cm1.id}/' , data={'body': 'newcomment'})
        force_authenticate(request, user=test_user2)
        response = view(request ,  pk = cm1.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_comment_delete(self): 
       
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        view = views.CommentDetail.as_view()
      
        request = self.factory.delete(f'api/advertisement/comments/{cm1.id}/')
        force_authenticate(request, user=self.test_user)
        response = view(request ,  pk = cm1.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_comment_delete_forbidden(self): 
       
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        view = views.CommentDetail.as_view()
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        request = self.factory.delete(f'api/advertisement/comments/{cm1.id}/')
        force_authenticate(request, user=test_user2)
        response = view(request ,  pk = cm1.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_comment_update_forbidden(self): 
       
        test_ad1 = ServiceAdvertisement.objects.create(Title='test-title1', owner=self.test_user, service_type='medical1')
        cm1 = Comment.objects.create(body = 'comment1' , post = test_ad1 , owner = self.test_user)
        view = views.CommentDetail.as_view()
        test_user2 = Account.objects.create_user('test_user2', "test2@example.com", "234567")
        request = self.factory.put(f'api/advertisement/comments/{cm1.id}/' , data={'body': 'newcomment'})
        force_authenticate(request, user=test_user2)
        response = view(request ,  pk = cm1.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_get_user_data(self): 
       
        view = views.CommentDetail.as_view()
       
        request = self.factory.get(f'api/advertisement/userview/{self.test_user.id}/')
        view = views.UserDetail.as_view()
        force_authenticate(request, user= self.test_user)
        response = view(request ,  pk = self.test_user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'] , self.test_user.username)
        self.assertEqual(response.data['email'] , self.test_user.email)
        
        
        
        
    
       
        
       
        
            
            
            
        
        
        
        
       
            
            
    
                
        
       
        
    
        
   
        
    

    
      

        


