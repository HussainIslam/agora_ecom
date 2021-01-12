from django.contrib import admin

from .models import (Product, 
                    P_Category, 
                    P_Image,
                    P_Color,
                    P_Size)

product_models = [Product, P_Category, P_Image, P_Color, P_Size]
admin.site.register(product_models)