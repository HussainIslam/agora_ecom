from rest_framework import serializers

from .models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.HyperlinkedRelatedField(view_name='cart', read_only=True)
    product = serializers.HyperlinkedRelatedField(view_name='product', read_only = True)
    color = serializers.HyperlinkedRelatedField(view_name='color', read_only = True)
    size = serializers.HyperlinkedRelatedField(view_name='size', read_only = True)

    class Meta:
        model = CartItem
        fields = '__all__'