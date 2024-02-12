from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products import models, serializers


@api_view(['GET'])
def index(request, *args, **kwargs):
    return Response(kwargs)


class ProductView(ModelViewSet):
    # serializer_class = serializers.ProductModelSerializer
    # queryset = models.Product.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.ProductListSerializer

        return serializers.ProductModelSerializer

    def get_queryset(self):
        return models.Product.objects.select_related('category')
