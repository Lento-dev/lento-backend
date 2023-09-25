from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user_account.api import views
from rest_registration.api.views import login, logout, register, verify_registration, send_reset_password_link, \
    reset_password, change_password

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('verify_registration/', verify_registration, name='verify_registration'),
    path('send_reset_password_link/', send_reset_password_link, name='send_reset_password_link'),
    path('reset_password/', reset_password, name='reset_password'),
    path('change_password/', change_password, name='change_password'),
    path('edit-profile/', views.UserProfileRetrieveUpdateView.as_view({'put': 'update'}), name='edit-profile'),
    path('user-profile/', views.UserProfileRetrieveUpdateView.as_view({'get': 'retrieve'}), name='user-profile'),
    path('access-phone/' , views.Access_phone_number , name = 'access_phone'),
    path('access-profile/' , views.Access_profile , name = 'access_profile'),
    path('verify-newemail/' , views.verification , name = 'verify'),
    path('changeEmail/' , views.changeEmail , name = 'change'),
    path('public-profile/<id>/', views.PublicUserProfileView.as_view({'get': 'retrieve'}), name='public-profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
