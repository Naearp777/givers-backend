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
        return Response(serializer.data)
    except:
        message={'detail':'Event with this content already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Event_display_specific(request,username):
    user = get_object_or_404(User.objects, username=username)
    event = Events.objects.filter(user=user)
    serializer=EventSerializer(event,many=True)
    return Response(serializer.data)
'''
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def Event_Update(request,name):
    try:
        event = Events.objects.get(name = name)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventSerializer(event , data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
'''

class EventRegister(APIView):
    queryset =Events.objects.all()
    serializer_class= EventSerializer

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)

class EventUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventUpdateSerializer

from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Events.objects.all()

