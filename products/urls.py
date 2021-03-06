from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='products'),
    path('products/<uuid:pk>/', views.ProductDetail.as_view(), name='product'),
    path('categories/', views.PCategoryList.as_view(), name='categories'),
    path('categories/<uuid:pk>/', views.PCategoryDetail.as_view(), name='category'),
    path('brands/', views.PBrandList.as_view(), name='brands'),
    path('brands/<uuid:pk>/', views.PBrandDetail.as_view(), name='brand'),
    path('colors/', views.PColorList.as_view(), name='colors'),
    path('colors/<uuid:pk>/', views.PColorDetail.as_view(), name='color'),
    path('sizes/', views.PSizeList.as_view(), name='sizes'),
    path('sizes/<uuid:pk>/', views.PSizeDetail.as_view(), name='size'),
    path('images/', views.PImageList.as_view(), name='images'),
    path('images/<uuid:pk>/', views.PImageDetail.as_view(), name='image'),
]
