from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser, Address

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['user_id', 'first_name', 'last_name', 'billing_address', 'shipping_address',
                    'date_of_birth', 'phone', 'email', 'password', 'gender', 'registered_on',
                    'last_modified', 'is_active', 'is_staff']

class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [ 'email', 'password' ]

    def create(self, validated_data):
        '''
        Method to create new user by calling the create_user method from manager
        '''
        return CustomUser.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)
    access = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError("Email address was not provided for login")

        if password is None:
            raise serializers.ValidationError("Password was not provided")

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError("A user with this email and password was not found")

        if not user.is_active:
            raise serializers.ValidationError("The user has been deactivated")
        
        tokens = RefreshToken.for_user(user)

        return {
            'email': user.email,
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }

class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    old_password = serializers.CharField(max_length=64)
    new_password = serializers.CharField(max_length=64)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'