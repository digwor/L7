from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    price = serializers.IntegerField(allow_null=True)
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    category_id = serializers.IntegerField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

class CategorySerializer(serializers):
    name = serializers.CharField()

class PartialUpdateProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    price = serializers.IntegerField(allow_null=True, required=False)
    description = serializers.CharField(required=False)
    quantity = serializers.IntegerField(required=False)
    category_id = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(required=False)

