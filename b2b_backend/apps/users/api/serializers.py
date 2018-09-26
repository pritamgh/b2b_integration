from ..models import CustomUser
# from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
# from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password',
                  'user_role', 'warehouse_exchange_id')


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

