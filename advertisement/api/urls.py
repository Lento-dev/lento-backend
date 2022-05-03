from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('addfood/', views.Foodcreate.as_view({'post': 'create'}), name='addfood'),
    path('addanimal/', views.animalcreate.as_view({'post': 'create'}), name='addanimal'),
    path('addservice/', views.Servicecreate.as_view({'post': 'create'}), name='addservice'),
    path('addcloth/', views.clothcreate.as_view({'post': 'create'}), name='addcloth'),
    path('delete/<id>/', views.DeleteAdvertisementView.as_view(), name='delete'),
    path('update-clothes/<id>/', views.UpdateClothesAdvertisementView.as_view(), name='update-clothes'),
    path('update-food/<id>/', views.UpdateFoodAdvertisementView.as_view(), name='update-food'),
    path('update-animal/<id>/', views.UpdateAnimalAdvertisementView.as_view(), name='update-animal'),
    path('update-service/<id>/', views.UpdateServiceAdvertisementView.as_view(), name='update-service'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
