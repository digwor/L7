from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0, db_default=0)
    description = models.TextField(null=True)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
