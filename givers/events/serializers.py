from rest_framework import serializers
from .models import Events

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'


class EventUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        exclude = ['user']

    def update(self, instance, validated_data): 
        # instance.user = validated_data.get('name', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        # instance.banner = validated_data.get( instance.banner)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.toggle = validated_data.get('toggle', instance.toggle)


        instance.save()
        return instance

