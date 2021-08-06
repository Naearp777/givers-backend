
from .models import requestform
from rest_framework import serializers
from events.serializers import EventSerializer
from volunteer.models import requestevents
from customuser.serializers import UserSerializer


class approvalSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True, many=False)
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = requestevents
        fields = '__all__'
        extra_kwargs = {'user': {'required': False},
                        'event': {'required': False}}


class requestedSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True, many=False)
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = requestevents
        fields = '__all__'


class RequestFormSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True, many=False)

    class Meta:
        model = requestform
        fields = '__all__'
