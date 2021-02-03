from rest_framework import generics

from .models import Shipper, Order, Orderline, Payment
from .serializers import ShipperSerializer, OrderSerializer, OrderlineSerializer, PaymentSerializer

class ShipperList(generics.ListCreateAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer

class ShipperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderlineList(generics.ListCreateAPIView):
    queryset = Orderline.objects.all()
    serializer_class = OrderlineSerializer

class OrderlineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orderline.objects.all()
    serializer_class = OrderlineSerializer

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer