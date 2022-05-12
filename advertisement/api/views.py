from rest_framework import generics, status, viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django_filters import rest_framework as django_filters
from .serializers import BaseAdvertisementSerializer, ServiceAdvertisementSerializer, FoodAdvertisementSerializer, \
    AnimalAdvertisementSerializer, ClothesAdvertisementSerializer, BaseAdvertisementPolymorphicSerializer
from advertisement.models import BaseAdvertisement, ServiceAdvertisement, FoodAdvertisement, AnimalAdvertisement, \
    ClothAdvertisement
from advertisement.permissions import IsOwner
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
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    lookup_field = 'id'


class SearchAdvertisementView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BaseAdvertisementPolymorphicSerializer
    queryset = BaseAdvertisement.objects.all()
    filter_backends = [filters.SearchFilter, django_filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilterSet
    search_fields = ['Title']
