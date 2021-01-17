from rest_framework import serializers

from .models import Shipper, Order, Orderline

class ShipperSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shipper
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class OrderlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orderline
        fields = '__all__'