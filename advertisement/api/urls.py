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
    path('retrieve/<id>' ,  views.AdvertisementViewSetretrieve.as_view({'get': 'retrieve'}) , name = 'retrieve'),
    path('create/' , views.AdvertisementViewSetretrieve.as_view({'post' : 'create'}) , name ='create-advertisement' ),
    path('comments/' , views.CommentList.as_view(), name="comments"),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name = "comment-detail"),
    path('commentposts/', views.Commentofpost.as_view(), name = "comment-post"),
    path('homepageads/' , views.AdvertisementViewSetreturn.as_view({'get': 'list'}) , name = 'list-all' ),
    path('userview/<int:pk>' , views.UserDetail.as_view() , name = 'user-detail' ),
    path('Saves/' , views.save_view2.as_view({'post': 'create'}), name="saves"),
    path('Savelist/', views.save_view2.as_view({'get': 'list'} , ), name = "saves-list"),
    path('Saves/<id>/', views.save_view2.as_view({'get': 'retrieve'} ), name = "saves-retrieve")
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
