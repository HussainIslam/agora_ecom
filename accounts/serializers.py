from rest_framework import serializers

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

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'