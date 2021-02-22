import uuid
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .managers import CustomUserManager



class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.street_address}'

class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    billing_address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True, related_name='billing_address')
    shipping_address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True, related_name='shipping_address')
    date_of_birth = models.DateField(auto_now_add=True, editable=True, blank=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True, max_length=128)
    password = models.CharField(_('password'), max_length=128)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ("Don't want to disclose", "Don't want to disclose"),
        ("Haven't mentioned", "Haven't mentioned")
    ]
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, default="Haven't mentioned", blank=True, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        first_name = "No first name registered"
        last_name = "No last name registered"
        if self.first_name != None: 
            first_name = self.first_name
        if self.last_name != None:
            last_name = self.last_name
        return '{} {}'.format(first_name, last_name)
    
