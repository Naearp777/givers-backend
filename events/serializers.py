from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Events
from customuser.models import User
from category.serializers import EventCategorySerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude=['password','admin']


class EventSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True,many=False)
    category=EventCategorySerializer(read_only=True,many=False)
    class Meta:
        model=Events
        fields='__all__'
class EventupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'