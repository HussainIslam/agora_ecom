from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Address

class CustomUserAdmin(UserAdmin):
    model = get_user_model()

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Address)
