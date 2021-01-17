from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CartList.as_view(), name='carts'),
    path('<uuid:pk>/', views.CartDetail.as_view(), name='cart'),
]
