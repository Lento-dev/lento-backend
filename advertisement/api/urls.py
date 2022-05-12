from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('addfood/', views.Foodcreate.as_view({'post': 'create'}), name='addfood'),
    path('addanimal/', views.animalcreate.as_view({'post': 'create'}), name='addanimal'),
    path('addservice/', views.Servicecreate.as_view({'post': 'create'}), name='addservice'),
    path('addcloth/', views.clothcreate.as_view({'post': 'create'}), name='addcloth'),
    path('update/<id>/', views.AdvertisementViewSet.as_view({'put': 'update'}), name='update-advertisement'),
    path('delete/<id>/', views.AdvertisementViewSet.as_view({'delete': 'destroy'}), name='delete-advertisement'),
    path('search/', views.SearchAdvertisementView.as_view(), name='search-advertisement'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
