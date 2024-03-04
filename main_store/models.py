from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
