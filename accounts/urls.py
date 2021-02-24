from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views

app_name='accounts'

urlpatterns = [
    path('addresses/', views.AddressList.as_view(), name='addresses'),
    path('addresses/<uuid:pk>/', views.AddressDetail.as_view(), name='address'),
    path('users/', views.UserRegistrationAPIView.as_view(), name='registration'),
    path('users/login/', views.UserLoginAPIView.as_view(), name='login'),
    path('users/logout/', views.UserLogoutAPIView.as_view(), name='logout')
]
