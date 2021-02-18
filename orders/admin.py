from django.contrib import admin

from .models import Shipper, Order, Orderline, Promotion, Payment

order_models = [Shipper, Order, Orderline, Promotion, Payment]

admin.site.register(order_models)