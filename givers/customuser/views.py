from rest_framework.fields import EmailField
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
    print(data)
    try:
        user=User.objects.create(
            password=make_password(data['password']),
            email=data['email'],
            full_name=data['full_name'],
            last_login=data['last_login'],
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
        message={'detail':'User already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)