from rest_framework import serializers

from .models import Shipper, Order, Orderline, Payment, Promotion

class ShipperSerializer(serializers.ModelSerializer):
    shipper_address = serializers.HyperlinkedRelatedField(read_only=True, view_name='address')

    class Meta:
        model = Shipper
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    shipper = serializers.HyperlinkedRelatedField(read_only=True, view_name='shipper')
    billing_address = serializers.HyperlinkedRelatedField(read_only=True, view_name='address')
    shipping_address = serializers.HyperlinkedRelatedField(read_only=True, view_name='address')
    customer = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Order
        fields = '__all__'

class OrderlineSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(read_only=True, view_name='order')
    product = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product')
    color = serializers.HyperlinkedRelatedField(read_only=True, view_name='color')
    size = serializers.HyperlinkedRelatedField(read_only=True, view_name='size')
    promotion = serializers.HyperlinkedRelatedField(read_only=True, view_name='promotion')

    class Meta:
        model = Orderline
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(read_only=True, view_name='order')

    class Meta:
        model = Payment
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = '__all__'