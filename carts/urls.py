from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CartList.as_view(), name='carts'),
    path('<uuid:pk>/', views.CartDetail.as_view(), name='cart'),
    path('cartitems/', views.CartItemList.as_view(), name='cartitems'),
    path('cartitems/<uuid:pk/', views.CartItemDetail.as_view(), name='cartitem')
]
