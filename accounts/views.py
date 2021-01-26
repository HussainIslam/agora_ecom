from rest_framework import generics

from .models import Address
from .serializers import AddressSerializer

class AddressList(generics.ListCreateAPIView):
    model = Address
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Address
    serializer_class = AddressSerializer