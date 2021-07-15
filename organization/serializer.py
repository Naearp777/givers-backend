
from rest_framework import serializers

from volunteer.models import requestevents


class approvalSerializer(serializers.ModelSerializer):
    class Meta:
        model=requestevents
        fields='__all__'
        extra_kwargs = {'user': {'required': False},'event': {'required': False}}


class requestedSerializer(serializers.ModelSerializer):
    class Meta:
        model=requestevents
        fields='__all__'