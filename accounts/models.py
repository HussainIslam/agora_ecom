import uuid
import datetime
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

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    billing_address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True, related_name='billing_address')
    shipping_address = models.ForeignKey(Address, on_delete=models.RESTRICT, blank=True, null=True, related_name='shipping_address')
    date_of_birth = models.DateField(auto_now_add=datetime.date.today(), editable=True, blank=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ("Don't want to disclose", "Don't want to disclose")
    ]
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, default="Don't want to disclose", blank=True, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email