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

