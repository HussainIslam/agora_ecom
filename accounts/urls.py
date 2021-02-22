from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('addresses/', views.AddressList.as_view(), name='addresses'),
    path('addresses/<uuid:pk>/', views.AddressDetail.as_view(), name='address'),
    path('users/', views.UserRegistrationAPIView.as_view(), name='registration')
]
