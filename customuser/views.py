from .serializers import UserSerializer,UserupdateSerializer
from .models import User
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
import pyotp
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

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
            active=data['active']

        )
        user=User.objects.get(email=data['email'])
        user.images=request.FILES.get('image')
        user.save()
        serializer=UserSerializer(user,many=False)

        email_template = render_to_string('signup_otp.html',{"otp":key['OTP'],"username":serializer.data['username'],"email":serializer.data['email']})    
        sign_up = EmailMultiAlternatives(
                        "Otp Verification", 
                        "Otp Verification",
                        settings.EMAIL_HOST_USER, 
                        [serializer.data['email']],
                    )
        sign_up.attach_alternative(email_template, 'text/html')
        sign_up.send()


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


@api_view(['POST'])
def RegisterVerify(request,otp):
    try:
        user = User.objects.get(otp = otp,active = False)
        otp = user.otp
        if otp != otp:
            return Response({"Otp" : "Invalid otp"},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            activation_key = user.activation_key
            totp = pyotp.TOTP(activation_key, interval=86400)
            verify = totp.verify(otp)
            
            if verify:
                user.active = True
                user.save()
                
                email_template = render_to_string('signup_otp_success.html',{"username":user.username})    
                sign_up = EmailMultiAlternatives(
                        "Account successfully activated", 
                        "Account successfully activated",
                        settings.EMAIL_HOST_USER, 
                        [user.email],
                    )
                sign_up.attach_alternative(email_template, 'text/html')
                sign_up.send()
                
                return Response({"Verify success" : "Your account has been successfully activated!!"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Time out" : "Given otp is expired!!"}, status=status.HTTP_408_REQUEST_TIMEOUT)
    
    except:
        return Response({"No User" : "Invalid otp OR No any inactive user found for given otp"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def Resend_otp(request,username):
    try:
        user=User.objects.get(username=username)
        serializer=UserSerializer(user,many=False)
        email_template = render_to_string('signup_otp.html',{"otp":serializer.data['otp'],"username":serializer.data['username'],"email":serializer.data['email']})    
        sign_up = EmailMultiAlternatives(
                        "Otp Verification", 
                        "Otp Verification",
                        settings.EMAIL_HOST_USER, 
                        [serializer.data['email']],
                    )
        sign_up.attach_alternative(email_template, 'text/html')
        sign_up.send()

        return Response(status=status.HTTP_200_OK)
    except User.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserupdateSerializer