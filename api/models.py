# from django.db import models
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.IntegerField(default=0, db_default=0)
#     description = models.TextField(null=True)
#     quantity = models.IntegerField()
#     category_id = models.IntegerField()
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=255)
