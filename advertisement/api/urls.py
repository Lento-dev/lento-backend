from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Foodcreate , animalcreate , Servicecreate, clothcreate

urlpatterns = [
    path('addfood/', Foodcreate.as_view({'post': 'create'}), name='addfood'),
    path('addanimal/', animalcreate.as_view({'post': 'create'}), name='addanimal'),
    path('addservice/', Servicecreate.as_view({'post': 'create'}), name='addservice'),
    path('addcloth/', clothcreate.as_view({'post': 'create'}), name='addcloth')
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
