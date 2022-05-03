from venv import create
from rest_framework import generics,status , viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import Advertisement , ServiceAd, FoodAd , animalAd , clothesAd 
from advertisement.models import BaseAdvertisement , ServiceAdvertisement , FoodAdvertisement , AnimalAdvertisement ,ClothAdvertisement
from drf_multiple_model.views import ObjectMultipleModelAPIView



class HomeAPIView(ObjectMultipleModelAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    
        
    def get_querylist(self):
        querylist = [
            {'queryset': FoodAdvertisement.objects.filter(owner = self.request.user.id ), 'serializer_class': FoodAd},
            {'queryset': ServiceAdvertisement.objects.filter(owner = self.request.user.id), 'serializer_class': ServiceAd},
            {'queryset': ClothAdvertisement.objects.filter(owner = self.request.user.id), 'serializer_class':clothesAd },]
        
        return  querylist; 
        

class Foodcreate(generics.CreateAPIView, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FoodAd
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
    serializer_class = ServiceAd
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
    serializer_class = animalAd
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
    serializer_class = clothesAd
    queryset = ClothAdvertisement.objects.all()

    def create(self, request, *args, **kwargs):
        serializer_data = request.data.copy()
        serializer_data.update({'owner':request.user.id})
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





















































