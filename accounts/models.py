import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models



class Address:
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

class CustomUser(AbstractUser):
    pass