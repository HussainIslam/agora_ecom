from django.contrib import admin

from .models import (Product, 
                    P_Category, 
                    P_Image,
                    P_Color)

product_models = [Product, P_Category, P_Image, P_Color]
admin.site.register(product_models)