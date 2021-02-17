import uuid
from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Address
from products.models import Product, P_Color, P_Size


class Shipper(models.Model):
    shipper_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    shipper_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=15, blank = True, null = True)
    email = models.EmailField()
    website = models.URLField()
    shipper_address = models.ForeignKey(Address, on_delete=models.RESTRICT, related_name='shipper_address')

    def __str__(self):
        return self.shipper_name

class Promotion(models.Model):
    promotion_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    promotion_name = models.CharField(max_length=200, blank = True, null = True)
    promotion_description = models.TextField(blank = True, null = True)
    minimum_purchase_amount = models.FloatField(blank = True, null = True)
    maximum_purchase_amount = models.FloatField(blank = True, null = True)
    discount_rate = models.FloatField(blank = True, null = True)
    discount_amount = models.FloatField(blank = True, null = True)
    free_delivery = models.BooleanField(default = False, blank = True, null = True)
    start_date = models.DateTimeField(blank = True, null = True)
    end_date = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.promotion_id

class Order(models.Model):
    order_id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable = False)
    date = models.DateTimeField(auto_now_add=True)
    billing_address = models.ForeignKey(Address, on_delete=models.RESTRICT, related_name='billing_address_order')
    shipping_address = models.ForeignKey(Address, on_delete=models.RESTRICT, related_name='shipping_address_order')
    bill_amount = models.FloatField(default=0.00)
    shipper = models.ForeignKey(Shipper, on_delete=models.RESTRICT, related_name='shipper_order')
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='customer_order')

    def __str__(self):
        return self.order_id

class Orderline(models.Model):
    orderline_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ManyToManyField(Product, related_name='product_orderline')
    quantity = models.FloatField()
    total_price = models.FloatField()
    color = models.ForeignKey(P_Color, on_delete=models.RESTRICT, related_name='color_orderline')
    size = models.ForeignKey(P_Size, on_delete=models.RESTRICT, related_name='size_orderline')
    promotion = models.ForeignKey(Promotion, on_delete=models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.orderline_id

class Payment(models.Model):
    payment_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
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
    order = models.OneToOneField(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.payment_id