from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=20)
    gender = models.CharField(max_length=5, default='male')
    adress = models.CharField(max_length=200, default='Tashkent')