from volunteer.models import requestevents
from .serializer import approvalSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customuser.models import User
from events.models import Events

# Create your views here.
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