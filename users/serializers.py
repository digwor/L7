from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class CreateTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User()
        fields = '__all__'
