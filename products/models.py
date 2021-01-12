import uuid
from django.db import models

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()
    note = models.TextField()
    price = models.FloatField(default=0.00)
    unit_of_measurement = models.CharField(max_length=20)
    quantity_in_stock = models.IntegerField()
    quantity_in_transit = models.IntegerField()
    quantity_ordered = models.IntegerField()
    quantity_per_unit = models.IntegerField()
    weight = models.FloatField()
    dimension = models.CharField(max_length=50)
    rating = models.FloatField(default=0.00)
    ranking = models.IntegerField(default=0)
    is_taxable = models.BooleanField(default=True)
    tax_rate = models.FloatField(default=0.13)

    def __str__(self):
        return self.product_name

class P_Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()
    product = models.ManyToManyField(Product, related_name='p_category')

    def __str__(self):
        return self.category_name
    
class P_Image(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_url = models.URLField(max_length=400)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class P_Color(models.Model):
    color_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color_name = models.CharField(max_length=20)
    color_code_hex = models.CharField(max_length=6, blank=True, null=True)
    product = models.ManyToManyField(Product, related_name='p_color')
