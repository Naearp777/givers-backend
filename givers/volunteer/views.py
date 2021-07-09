from django.shortcuts import render,get_object_or_404
from rest_framework import response
from .models import requestevents
from .serializers import requesteventSerializervolunteer,approvalSerializer
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from customuser.models import User
from events.models import Events
# Create your views here.

@api_view(['POST'])
def requestevent(request):
    data=request.data
    try:
        requestevent=requestevents.objects.create(
            user=User.objects.get(username=data['username']),
            event=Events.objects.get(name=data['name']),
            description=data['description'],
            interested=data['interested'],
            request_volunteer=data['request_volunteer'],
        )
        serializer=requesteventSerializervolunteer(requestevent,many=False)
        requestevent=requestevents.objects.get(id=serializer.data['id'])
        requestevent.user_details=request.FILES.get('user_details')
        requestevent.save()
        serializer=requesteventSerializervolunteer(requestevent,many=False)
        
        return Response(serializer.data)
    except:
        message={'detail':'requestevents with this content already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def showrequest(request,E_id,V_id):
    try:
        approval=requestevents.objects.filter(user_id=V_id ,event_id=E_id)
        serializer=approvalSerializer(approval,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def approval(request,E_id,V_id):
    try:
        approval=requestevents.objects.get(user_id=V_id ,event_id=E_id)
        serializer=approvalSerializer(approval,data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response (serializer.data)
        else:
            return Response ({'status':'Failed'})
    except requestevents.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
    