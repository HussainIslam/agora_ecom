import jwt
from django.conf import settings
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Address, CustomUser
from .serializers import (AddressSerializer, UserRegistrationSerializer, UserLoginSerializer, CustomUserSerializer, ChangePasswordSerializer)
from .renderers import UserLoginJSONRenderer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginAPIView(APIView):
    #renderer_classes = (UserLoginJSONRenderer, )
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserLogoutAPIView(APIView):

    def post(self, request):
        try:
            refresh_token = request.META.get("HTTP_REFRESH")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(data={"message": "Successfully logged out of agora"},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordAPIView(APIView):
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        access=request.META.get('HTTP_AUTHORIZATION')
        decoded_access = jwt.decode(access, settings.SECRET_KEY, algorithms=["HS256"])
        self.user = CustomUser.objects.get(user_id=decoded_access['user_id'])
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if not self.user.check_password(old_password):
                return Response(data={"message": "That is not the correct password"}, status=status.HTTP_403_FORBIDDEN)
            self.user.set_password(serializer.data.get("new_password"))
            self.user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={"message": "Failed to change password"}, status=status.HTTP_400_BAD_REQUEST)
        
