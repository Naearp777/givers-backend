from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


# Create your views here.

@api_view(['POST'])
def registerUser(request):
    data=request.data
    try:
        user=User.objects.create(
            password=make_password(data['password']),
            email=data['email'],
            full_name=data['full_name'],
            last_login=data['last_login'],
            username=data['username'],
            address=data['address'],
            phone=data['phone'],
            facebook=data['facebook'],
            instagram=data['instagram'],
            twitter=data['twitter'],
            website=data['website'],
            description=data['description'],
            volunteer=data['volunteer'],
            organization=data['organization'],
            admin=data['admin']
        )
        user=User.objects.get(email=data['email'])
        user.images=request.FILES.get('image')
        user.save()
        serializer=UserSerializer(user,many=False)
        return Response(serializer.data)
    except:
        if(User.objects.get(email=data['email'])):
            if(User.objects.get(username=data['username'])):
                data={"message":"Email and Username already exists"}
            else:
                data={"message":"Email already exists"}
        else:
            data={"message":"Username already exists"}

        return Response(data,status=status.HTTP_400_BAD_REQUEST)