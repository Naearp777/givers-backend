from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
import pyotp

# Create your views here.
class generateKey:
    @staticmethod
    def returnValue():
        secret = pyotp.random_base32()        
        totp = pyotp.TOTP(secret, interval=86400)
        OTP = totp.now()
        return {"totp":secret,"OTP":OTP}

@api_view(['POST'])
def registerUser(request):
    key = generateKey.returnValue()
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
            admin=data['admin'],
            otp = key['OTP'],
            activation_key = key['totp'],

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