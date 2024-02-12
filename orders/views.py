from django.db.models import Prefetch
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class OrderViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Order.objects.prefetch_related(
        Prefetch(
            'order_items',
            queryset=models.OrderItem.objects.select_related('product')
        ),
    )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.OrderRetrieveSerializer

        return serializers.OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = models.OrderItem.objects.order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.OrderItemRetrieveSerializer

        if self.action == 'create':
            return serializers.OrderItemCreateSerializer

        return serializers.OrderItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_item = models.OrderItem.objects.create(
            order=serializer.validated_data['order'],
            product=serializer.validated_data['product'],
            price=serializer.validated_data['product'].price,
        )

        serializer = serializers.OrderItemSerializer(order_item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
