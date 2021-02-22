from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer, UserRegistrationSerializer, CustomUserSerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        print(request.data)
        user = request.data.get('user', {})
        print(user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)