from rest_framework import generics, status, viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django_filters import rest_framework as django_filters

from user_account.models import Account
from .serializers import BaseAdvertisementSerializer, ServiceAdvertisementSerializer, FoodAdvertisementSerializer, \
    AnimalAdvertisementSerializer, ClothesAdvertisementSerializer, BaseAdvertisementPolymorphicSerializer, \
    CommentSerializer, SavedSerializer, UpdateBaseAdvertisementPolymorphicSerializer , userserializer
from advertisement.models import BaseAdvertisement, ServiceAdvertisement, FoodAdvertisement, AnimalAdvertisement,  \
    ClothAdvertisement  ,Comment , Saved
from advertisement.permissions import IsOwner , IsOwnerOrReadOnly
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
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    lookup_field = 'id'

class AdvertisementViewSetreturn(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    lookup_field = 'id'
    def get_queryset(self):
        return BaseAdvertisement.objects.order_by('date_joined')[:20]


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
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    #get_replies() function 
   

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class savedview( viewsets.ModelViewSet):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    response = {}

    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'user':request.user.id})
        postid = serializer_data['post']
        response = {}
        x = None
        try:
            keyword = '' 
            x = Saved.objects.get(user = request.user.id , post = postid)
            response['post'] = postid
            
            if(x.saved == True): 
                x.saved = False 
                keyword = 'False'
            else: 
                x.saved = True
                keyword = 'True'

            x.save()
            response['savepost'] = 'Save post is ' + keyword
            
        except: 
            print('data is not created yet or is not correct')

        if (x == None): 
            serializer_data.update({'saved':True})
            serializer = self.get_serializer(data=serializer_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = serializer_data
            response.update({'savedpost':'Save post is True'})
            
        return Response(response, status=status.HTTP_201_CREATED)


    def get_queryset(self): 
        
        queryset = Saved.objects.filter(user = self.request.user.id  , saved = True); 
        return queryset; 

    def get_object(self): 
        postid = self.request.GET.get('post')
        return Saved.objects.get(user = self.request.user.id , post = postid)

    def retrieve(self, request): 
        data = {}
        postid = self.request.GET.get('post')
        
        s = status.HTTP_200_OK
       
        try: 
            obj = self.get_object(); 
            savedx = obj.saved
            data['save'] = savedx
             
        except: 
            data['save'] = False

        if(postid.isnumeric()):
             get_object_or_404(BaseAdvertisement ,  id = postid)
        else: 
            data = {'status':'bad data format'}
            s = status.HTTP_400_BAD_REQUEST
        return  Response(data, s)
    
    
