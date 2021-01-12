import uuid
from django.db import models

from accounts.models import CustomUser, Address
from products.models import Product, P_Color, P_Size


class Shipper(models.Model):
    shipper_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    shipper_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=15, blank = True, null = True)
    email = models.EmailField()
    website = models.URLField()
    shipper_addess = models.ForeignKey(Address, on_delete=models.RESTRICT, related_name='shipper_address')


class Order(models.Model):
    order_id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable = False)
    date = models.DateTimeField(auto_now_add=True)
    billing_address = models.ForeignKey(Address, on_delete=models.RESTRICT, related_name='billing_address_order')
    shipping_address = models.ForeignKey(Address, on_delete=models.RESTRICT, related_name='shipping_address_order')
    bill_amount = models.FloatField(default=0.00)
    PAYMENT_METHOD_CHOICES = [
        ('Mastercard', 'Mastercard'),
        ('Visa', 'Visa'),
        ('Paypal', 'Paypal'),
        ('Interac', 'Interac'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='Visa',blank=False, null=False)
    payment_date = models.DateTimeField(auto_now=True)
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Unpaid', blank=False, null=False)
    payment_amount = models.FloatField(default=0.00)
    shipper = models.ForeignKey(Shipper, on_delete=models.RESTRICT, related_name='shipper_order')
    tracking_number = models.CharField(max_length=50, blank=True, null=True)


class Orderline(models.Model):
    orderline_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ManyToManyField(Product, related_name='product_orderline')
    quantity = models.FloatField()
    total_price = models.FloatField()
    color = models.ForeignKey(P_Color, on_delete=models.RESTRICT, related_name='color_orderline')
    size = models.ForeignKey(P_Size, on_delete=models.RESTRICT, related_name='size_orderline')
