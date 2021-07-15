from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ChangePasswordSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser

from customuser.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework import generics

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

from django.contrib.auth.tokens  import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,  urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user=request.user
    serializer=UserSerializer(user,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def registerUser(request):
    data=request.data
    try:
        user=User.objects.create(
            first_name=data['name'],
            username=data['name'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer=UserSerializerWithToken(user,many=False)
        return Response(serializer.data)
    except:
        message={'detail':'user with this email already exists'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data=super().validate(attrs)
        serializer=UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k]=v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user=request.user
    serializer=UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (AllowAny)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse  
from django.conf import settings
import os      
from django.template.loader import render_to_string, get_template
def my_mail(request):  
    subject = "Greetings from Programink"  
    msg_html = render_to_string('email_send.html')
    
    with open(os.path.join(settings.BASE_DIR, 'templates\email_send.html')) as f:
        message = f.read()
    
    msg     = "template/email_send.html"  
    to      = "saugatkafley@gmail.com"  
    res     = EmailMultiAlternatives(subject,msg_html,settings.EMAIL_HOST_USER,[to])  
    res.content_subtype = "html"  # Main content is now text/html
    res.send()
    if(res == 1):  
        msg = "Mail Sent Successfully."  
    else:  
        msg = "Mail Sending Failed."  
    return HttpResponse(msg)  


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        data = {'request':request, 'data': request.data}
        serializer = self.serializer_class(data = data)
        serializer.is_valid(raise_exception=True)

        email = request.data['email']
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            subject = "Greetings from Givers!"
            current_site = get_current_site(
                request  = request).domain
            relativeLink = reverse('password_reset_confirm', kwargs={'uidb64':uidb64, 'token':token})
            absurl = 'http://' + current_site + relativeLink 
            email_body = 'Hi' + user.full_name+ 'Use this Link below to verify your email\n'+ absurl
            send_mail(subject,email_body,settings.EMAIL_HOST_USER, [user.email])
            return Response({'sucess': "We have sent a password reset email"}, status= status.HTTP_200_OK)

class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self,request, uidb64,token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id = id)

            if not PasswordResetTokenGenerator().check_token(user,token):
                 return Response({'error': "Token is not valid"}, status= status.HTTP_401_UNAUTHORIZED)

            return Response ({'sucess':True, 'message': 'Credentials are valid.', 'uidb64': uidb64, 'token':token}, status= status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as  identifier:
            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({'error': "Token is not valid"}, status= status.HTTP_401_UNAUTHORIZED)

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
