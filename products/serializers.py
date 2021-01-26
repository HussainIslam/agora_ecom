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
    colors = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='color')
    sizes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='size')
    categories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='category')
    brand = serializers.HyperlinkedRelatedField(read_only=True, view_name='brand')

    class Meta:
        model = Product
        fields = '__all__'

class PCategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.HyperlinkedRelatedField(read_only=True, view_name='category')

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

class PSizeSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(read_only=True, view_name='category')


    class Meta:
        model = P_Size
        fields = '__all__'

class PImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = P_Image
        fields = '__all__'