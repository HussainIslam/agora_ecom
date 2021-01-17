from rest_framework import serializers

from .models import Shipper, Order, Orderline

class ShipperSerializer(serializers.ModelSerializer):
    model = Shipper
    fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    model = Order
    fields = '__all__'

class OrderlineSerializer(serializers.ModelSerializer):
    model = Orderline
    fields = '__all__'