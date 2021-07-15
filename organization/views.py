from volunteer.models import requestevents
from .serializer import approvalSerializer,requestedSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
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



@api_view(['GET'])
def show_all_requested(request,E_id):
    try:
        requested=requestevents.objects.filter(event_id=E_id,request_volunteer=True)
        serializer=requestedSerializer(requested,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except requestevents.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)

from notifications.signals import notify
from notification.models import Notification

@api_view(['GET', 'PUT'])
def update_request_api(request,E_id):
    if request.method == 'PUT':
        obj = requestevents.objects.get(event_id=E_id)
        serializer=approvalSerializer(obj, many=False)

        user = serializer.data['user']
        if serializer.is_valid():
            serializer.save()
            notify.send(request.user, recipient=user, verb='Your request has been approved.')
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

from notifications.signals import notify
class UpdateRequestAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = requestevents.objects.all()
    serializer_class = approvalSerializer

    #update and check if it is approved then notify user

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data['approved']== True:
                notify.send(self.request.user, recipient=obj.user, verb='Your request has been approved.')
                print("Your request has been approved")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                notify.send(self.request.user, recipient=obj.user, verb='Your request has been rejected.')
                print("Your request has been rejected")
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            

                
                





    






    
    
    

