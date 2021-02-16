from django.contrib import admin

from .models import Cart, CartItem

cartModels = [ Cart, CartItem ]

admin.site.register(cartModels)