from urllib import request
from venv import create
from winreg import QueryInfoKey
# from xxlimited import foo
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BaseAdvertisementSerializer, ServiceAdvertisementSerializer, FoodAdvertisementSerializer, \
    AnimalAdvertisementSerializer, ClothesAdvertisementSerializer, BaseAdvertisementPolymorphicSerializer
from advertisement.models import BaseAdvertisement, ServiceAdvertisement, FoodAdvertisement, AnimalAdvertisement, \
    ClothAdvertisement
from advertisement.permissions import IsOwner


class HomeAPIView(ObjectMultipleModelAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    
        
    def get_querylist(self):
        querylist = [
            {'queryset': FoodAdvertisement.objects.filter(owner = self.request.user.id ), 'serializer_class':  FoodAdvertisementSerializer},
            {'queryset': ServiceAdvertisement.objects.filter(owner = self.request.user.id), 'serializer_class': ServiceAdvertisementSerializer},
            {'queryset': ClothAdvertisement.objects.filter(owner = self.request.user.id), 'serializer_class':ClothesAdvertisementSerializer },]
        
        return  querylist; 
        



		
	
		
		
	# except(TypeError, ValueError, OverflowError, Token.DoesNotExist):
	# 	token1=None
	# 	return Response('Token is invalid or expired. Please request another confirmation email by signing in.', status=status.HTTP_400_BAD_REQUEST)
	
	# except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
	# 	user = None 
	# 	if user is None:
	# 		return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
	



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
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    lookup_field = 'id'

#with bug 

class adDetail(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class =  BaseAdvertisementPolymorphicSerializer
    permission_classes = [IsAuthenticated, IsOwner]
          
    def get_object(self):
        pk =  self.request.GET.get("id") 
        print(pk)
        object = None
        try: 
            food = FoodAdvertisement.objects.get(id= pk)
            object = food

        except: 
                object = None
            
        try:
            service = ServiceAdvertisement.objects.get(id= pk)
            object = service
        except: 
            object = None
            

        try:
            cloth = ClothAdvertisement.objects.get(id= pk)
            object = cloth
        except: 
            object = None

        try:
            animaal = AnimalAdvertisement.objects.get(id = pk)
            object = cloth
        except: 
            object = None
      
        return object




