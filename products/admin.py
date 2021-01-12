from django.contrib import admin

from .models import (Product, 
                    P_Category, 
                    P_Image,)

product_models = [Product, P_Category, P_Image]
admin.site.register(product_models)