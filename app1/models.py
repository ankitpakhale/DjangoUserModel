from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    # add additional fields in here

    def __str__(self):
        return self.name