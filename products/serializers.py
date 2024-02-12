from rest_framework import serializers

from . import models


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    category_id = serializers.IntegerField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Product
        fields = '__all__'
