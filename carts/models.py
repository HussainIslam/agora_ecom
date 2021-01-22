import uuid
from django.db import models

from products.models import Product
from accounts.models import CustomUser

class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_cart')

    def __str__(self):
        return self.customer

class CartItem(models.Model):
    cartitem_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.FloatField(default=0.00)
    added_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, related_name='product_cart')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_cartitem')
    