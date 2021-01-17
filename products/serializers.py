from rest_framework import serializers

from .models import (
    P_Category,
    P_Brand,
    P_Color,
    P_Size,
    Product,
    P_Image,
)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class PCategorySerialier(serializers.ModelSerializer):

    class Meta:
        model = P_Category
        fields = '__all__'

class PBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = P_Brand
        fields = '__all__'

class PColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = P_Color
        fields = '__all__'