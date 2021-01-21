import uuid
from django.db import models

class P_Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.category_name


class P_Brand(models.Model):
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_name = models.CharField(max_length=40)
    brand_description = models.TextField()
    brand_logo = models.ImageField(blank=True, null=True)
    brand_website = models.URLField(blank=True, null=True)


class P_Color(models.Model):
    color_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color_name = models.CharField(max_length=20)
    color_code_hex = models.CharField(max_length=6, blank=True, null=True)


class P_Size(models.Model):
    size_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(P_Category, on_delete=models.CASCADE, related_name='category_size')
    value = models.CharField(max_length=10)

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
    colors = models.ManyToManyField(P_Color, related_name='colors_product')
    sizes = models.ManyToManyField(P_Size, related_name='sizes_product')
    categories = models.ManyToManyField(P_Category, related_name='categories_product')
    brand = models.ForeignKey(P_Brand, on_delete=models.CASCADE, related_name='brand_product', blank=True, null=True)

    def __str__(self):
        return self.product_name


class P_Image(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
