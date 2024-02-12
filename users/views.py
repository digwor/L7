from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from . import serializers, exceptions

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create_token':
            return serializers.CreateTokenSerializer

        return serializers.UserSerializer

    @action(detail=False, url_path='logon', methods=['POST'])
    def create_token(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.filter(username=serializer.validated_data['username'])

        if not users.exists():
            raise exceptions.UsernameNotFoundError

        user = users.first()

        if not user.check_password(serializer.validated_data['password']):
            raise exceptions.InvalidCredentialError

        return Response(serializer.data, status=status.HTTP_201_CREATED)
