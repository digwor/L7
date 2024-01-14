from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from products import models, serializers


@api_view()
def index(request, *args, **kwargs):

    return Response({"message": "OK"})


class ProductView(ViewSet):

    def list(self, request):
        queryset = models.Product.objects.all()
        serializer = serializers.ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = models.Product.objects.create(**serializer.validated_data)
        data = serializers.ProductSerializer(product).data

        return Response(data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        product = models.Product.objects.get(pk=pk)
        serializer = serializers.ProductSerializer(product)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs['pk']
        product = models.Product.objects.get(pk=pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        serializer = serializers.ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pk = kwargs['pk']
        product = models.Product.objects.get(pk=pk)
        product.name = serializer.validated_data['name']
        product.price = serializer.validated_data['price']
        product.description = serializer.validated_data['description']
        product.quantity = serializer.validated_data['quantity']
        product.category_id = serializer.validated_data['category_id']
        product.is_active = serializer.validated_data['is_active']
        product.save(update_fields=('name', 'price', 'description', 'quantity', 'category_id', 'is_active'))

        data = serializers.ProductSerializer(product).data

        return Response(data)

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs['pk']
        product = models.Product.objects.get(pk=pk)

        serializer = serializers.PartialUpdateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        for key, value in serializer.validated_data.items():
            setattr(product, key, value)

        product.save()
        data = serializers.PartialUpdateProductSerializer(product).data

        return Response(data)

