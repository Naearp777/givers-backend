from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from rest_framework import status
from rest_framework import generics

from .models import Notification
from .serializers import NotificationSerializer,Request_as_volunteerSerializer
from events.models import Request_as_Volunteer
# Create your views here.

# Create a class to view notification inheriting from generics.RetrieveAPIView

class NotificationsAPI(generics.RetrieveAPIView):
    # set the queryset to the notifications
    queryset = Notification.objects.all()
    # set the serializer class
    serializer_class = NotificationSerializer

@api_view(['GET'])
def ShowNotifications(request):
        user = request.user
        notification = Notification.objects.filter(user = user).order_by('-date')
        # notification = Request_as_Volunteer.objects.all()
        serializer = NotificationSerializer(notification, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 


    

