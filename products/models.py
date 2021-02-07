import uuid
from django.db import models
from datetime import date
from django.utils import timezone

class P_Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()
    banner = models.ImageField(upload_to='category/', blank = True, null = True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.category_name


class P_Brand(models.Model):
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_name = models.CharField(max_length=40)
    brand_description = models.TextField()
    brand_logo = models.ImageField(upload_to="brands/",blank=True, null=True)
    brand_website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.brand_name


class P_Color(models.Model):
    color_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color_name = models.CharField(max_length=20)
    color_code_hex = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.color_name


class P_Size(models.Model):
    size_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(P_Category, on_delete=models.CASCADE, related_name='category_size')
    value = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.value} of {str(self.category)}'

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()
    note = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.00)
    unit_of_measurement = models.CharField(max_length=20)
    quantity_in_stock = models.IntegerField()
    quantity_in_transit = models.IntegerField()
    quantity_ordered = models.IntegerField()
    quantity_per_unit = models.IntegerField(default=1)
    weight = models.FloatField()
    dimension = models.CharField(max_length=50)
    rating = models.FloatField(default=0.00)
    ranking = models.IntegerField(default=0)
    is_taxable = models.BooleanField(default=True)
    tax_rate = models.FloatField(default=0.13, null=True, blank=True)
    colors = models.ManyToManyField(P_Color, related_name='colors_product', blank=True)
    sizes = models.ManyToManyField(P_Size, related_name='sizes_product', blank=True)
    categories = models.ManyToManyField(P_Category, related_name='categories_product', blank=True)
    brand = models.ForeignKey(P_Brand, on_delete=models.CASCADE, related_name='brand_product', blank=True, null=True)

    def __str__(self):
        return self.product_name

def product_image_path(instance, filename):
    return f'products/{date.today().year}/{date.today().month}/{instance.product.product_id}/{filename}'

class P_Image(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=product_image_path,blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")

    def __str__(self):
        return f'Image for {str(self.product)}'
