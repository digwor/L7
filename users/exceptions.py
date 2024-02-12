from rest_framework import status
from rest_framework.exceptions import APIException


class UsernameNotFoundError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'User name not exists'
    default_code = 'username not found'


class InvalidCredentialError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'User name or password is incorrect'
    default_code = 'invalid_credentials'
