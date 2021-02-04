from django.urls import path

from . import views

urlpatterns = [
    path('shippers/', views.ShipperList.as_view(), name='shippers'),
    path('shippers/<uuid:pk>/', views.ShipperDetail.as_view(), name='shipper'),
    path('orders/', views.OrderList.as_view(), name='orders'),
    path('orders/<uuid:pk>/', views.OrderDetail.as_view(), name='order'),
    path('orderlines/', views.OrderlineList.as_view(), name='orderlines'),
    path('orderlines/<uuid:pk>/', views.OrderlineDetail.as_view(), name='orderline'),
    path('payments/', views.PaymentList.as_view(), name='payments'),
    path('payments/<uuid:pk>/', views.PaymentDetail.as_view(), name='payment'),
    path('promotions/', views.PromotionList.as_view(), name='promotions'),
    path('promotions/<uuid:pk>/', views.PromotionDetail.as_view(), name='promotion')
]
