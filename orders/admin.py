from django.contrib import admin

from .models import Shipper, Order, Orderline

order_models = [Shipper, Order, Orderline]

admin.site.register(order_models)