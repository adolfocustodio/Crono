from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=250)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
