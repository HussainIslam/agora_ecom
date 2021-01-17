from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<uuid:pk>/', ProductDetail, name='product')
]
