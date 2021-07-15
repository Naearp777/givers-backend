from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customuser.models import User
from events.models import Events
from rest_framework import status
from events.serializers import EventSerializer
# Create your views here.
@api_view(['GET'])
def show_specific_category(request,category_id):
    try:
        category=Events.objects.filter(category=category_id)
        serializer=EventSerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Events.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)