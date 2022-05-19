from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Foodcreate , animalcreate , Servicecreate, clothcreate 
    
from . import views

urlpatterns = [
    path('addfood/', views.Foodcreate.as_view({'post': 'create'}), name='addfood'),
    path('addanimal/', views.animalcreate.as_view({'post': 'create'}), name='addanimal'),
    path('addservice/', views.Servicecreate.as_view({'post': 'create'}), name='addservice'),
    path('addcloth/', views.clothcreate.as_view({'post': 'create'}), name='addcloth'),
    path('update/<id>/', views.AdvertisementViewSet.as_view({'put': 'update'}), name='update-advertisement'),
    path('delete/<id>/', views.AdvertisementViewSet.as_view({'delete': 'destroy'}), name='delete-advertisement'),
    path('search/', views.SearchAdvertisementView.as_view(), name='search-advertisement'),
    path('load-all/', views.LoadViewSet.as_view({'get': 'list'}), name = 'get-advertisement'),
    path('retrieve/<id>' ,  views.AdvertisementViewSet.as_view({'get': 'retrieve'}) , name = 'retrieve'),
    path('create/' , views.AdvertisementViewSet.as_view({'post' : 'create'}) , name ='create-advertisement' ),
    path('comments/' , views.CommentList.as_view(), name="comments"),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name = "comment-detail"),
    path('save/', views.savedview.as_view({'post': 'create'}  ), name = "save-create"),
    path('savelist/', views.savedview.as_view({'get': 'list'} , ), name = "save-list"), 
    path('saveretrieve/', views.savedview.as_view({'get': 'retrieve'} , ), name = "save-retrieve"),
    path('homepageads/' , views.AdvertisementViewSet.as_view({'get': 'list'}) , name = 'list-all' ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
