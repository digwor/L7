import random
import uuid

# from django.contrib.auth import get_user_model
from django.db import models


# User = get_user_model()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def generate_number(cls) -> str:
        number = ''.join(random.choices('0123456789', k=8))

        if not cls.objects.filter(number=number).exists():
            return number

        return cls.generate_number()


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items',
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='order_items'
    )

    price = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
