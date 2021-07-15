# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.views import generic
from rest_framework.views import APIView
from .models import Events
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import status
from rest_framework import generics
from customuser.models import User

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def Event_display_all(request):
    all_events=Events.objects.all()
    serializer=EventSerializer(all_events,many=True)
    return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def Event_display_id(request,E_id):
    event=Events.objects.get(id=E_id)
    serializer=EventSerializer(event,many=False)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Event_display_specific(request,username):
    user = User.objects.get(username=username)
    event = Events.objects.filter(user=user)
    serializer=EventSerializer(event,many=True)
    return Response(serializer.data)

from notifications.signals import notify
@api_view(['POST'])
def registerEvent(request):
    data=request.data
    try:
        Event=Events.objects.create(
            user=User.objects.get(username=data['username']),
            name=data['name'],
            location=data['location'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            description=data['description'],
            toggle=data['toggle'],
        )
        serializer=EventSerializer(Event,many=False)
        Event=Events.objects.get(id=serializer.data['id'])
        Event.banner=request.FILES.get('banner')
        Event.save()
        serializer=EventSerializer(Event,many=False)
        notify.send(sender=request.user,recipient=User.objects.get(username=data['username']),verb='created an event',level='info',target=Event)
        return Response(serializer.data)
    except:
        message={'detail':'Event with this content already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

class RegisterEventAPI(generics.CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)
    queryset = Events.objects.all()

    def perform_create(self, serializer):
        notify.send(sender = self.request.user,recipient  =User.objects.filter(volunteer= self.request.user.volunteer) , verb = " There is an event created.")
        serializer.save(user=self.request.user)

        # notify.send(self.request.user,recipient = self. ,verb='There is a new event .',level='info',target=serializer.save())
        # serializer.save(user=self.request.user)
        




