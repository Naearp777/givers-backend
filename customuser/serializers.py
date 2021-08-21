from rest_framework import  serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login']


class UserupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login']


class UserresendotpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
