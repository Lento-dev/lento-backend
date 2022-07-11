
from lib2to3.pytree import Base
from urllib import response
from jsonschema import ValidationError
from rest_framework import generics, status, viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django_filters import rest_framework as django_filters
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from user_account.models import Account
from .serializers import BaseAdvertisementSerializer, ServiceAdvertisementSerializer, FoodAdvertisementSerializer, \
    AnimalAdvertisementSerializer, ClothesAdvertisementSerializer, BaseAdvertisementPolymorphicSerializer, \
    CommentSerializer, UpdateBaseAdvertisementPolymorphicSerializer , userserializer , SavedmodelSerializer , SaveAdvertisementDatas
from advertisement.models import BaseAdvertisement, ServiceAdvertisement, FoodAdvertisement, AnimalAdvertisement,  \
    ClothAdvertisement  ,Comment ,  SavedModel
from advertisement.permissions import IsOwner , IsOwnerOrReadOnly , SaveIsOwner ,  ReadOnlyuser
from django.shortcuts import render, get_object_or_404, redirect
from advertisement.filtersets import AdvertisementFilterSet

class Foodcreate(generics.CreateAPIView, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FoodAdvertisementSerializer
    queryset = FoodAdvertisement.objects.all()


    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'owner':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Servicecreate(generics.CreateAPIView, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceAdvertisementSerializer
    queryset = ServiceAdvertisement.objects.all()
    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'owner':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class animalcreate(generics.CreateAPIView, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AnimalAdvertisementSerializer
    queryset = AnimalAdvertisement.objects.all()


    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'owner':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class clothcreate(generics.CreateAPIView, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ClothesAdvertisementSerializer
    queryset = ClothAdvertisement.objects.all()

    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'owner':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AdvertisementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwner]
    serializer_class = UpdateBaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    lookup_field = 'id'




class AdvertisementViewSetretrieve(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    lookup_field = 'id'

class AdvertisementViewSetreturn(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    lookup_field = 'id'
    def get_queryset(self):
        return BaseAdvertisement.objects.order_by('-date_joined')[:20]


class SearchAdvertisementView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    filter_backends = [filters.SearchFilter, django_filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilterSet
    search_fields = ['Title']


class LoadViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    lookup_field = 'id'
    def get_queryset(self): 
        return BaseAdvertisement.objects.filter(owner = self.request.user.id)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = userserializer 
    permission_classes = [ ReadOnlyuser]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    #get_replies() function 
   

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class Commentofpost(generics.ListAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        postid = self.request.GET.get('post')
        return Comment.objects.filter(post = postid)
   


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



class save_view2( viewsets.ModelViewSet):
    queryset = SavedModel.objects.all()
    serializer_class = SavedmodelSerializer
    permission_classes = [IsAuthenticated,  SaveIsOwner]
    lookup_field = 'id'
    response = {}
    
    def create(self, request, *args, **kwargs): 
        serializer_data = request.data.copy()
        postid = serializer_data['post_n']
        save_option = None
        try:
            save_option = SavedModel.objects.get(user_n = self.request.user.id , post_n = postid)
        except: 
            save_option = None
        
       
        if save_option is None: 
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            self.response = serializer_data
            self.response['save'] = 'save'
        else: 
            save_option.delete()
            self.response['save'] = 'unsave'
            self.response['post_n'] = postid
        return Response(self.response , status=status.HTTP_201_CREATED)
       

        
        
    def perform_create(self, serializer):
        
        serializer.save(user_n=self.request.user)
      

    def get_queryset(self): 
        
        queryset = SavedModel.objects.filter(user_n = self.request.user.id ); 
        return queryset; 

      
     
class save_view3( viewsets.ModelViewSet):
    queryset = SavedModel.objects.all()
    serializer_class = SaveAdvertisementDatas
    permission_classes = [IsAuthenticated,  SaveIsOwner]
    lookup_field = 'id'

    def get_queryset(self): 
       return SavedModel.objects.filter(user_n = self.request.user.id ); 
    
        
        
    
   
   
   
    
    
