from rest_framework import generics

from .models import Shipper, Order, Orderline
from .serializers import ShipperSerializer, OrderSerializer, OrderlineSerializer

class ShipperList(generics.ListCreateAPIView):
    queryset = Shipper
    serializer_class = ShipperSerializer

class ShipperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipper
    serializer_class = ShipperSerializer

