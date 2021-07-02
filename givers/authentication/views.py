from django.shortcuts import render
from .serializers import UserSerializer, UserSerializerWithToken, ChangePasswordSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser

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


# Create your views here.
'''
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def auth_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)
'''


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
    #@classmethod
    #def get_token(cls, user):
    #   token = super().get_token(user)
    
    #Validation ....next topic 
    def validate(self,attrs):
        data=super().validate(attrs)
        serializer=UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k]=v
        return data
        # Add custom claims
        #token['name'] = user.name
        # ...
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    


@api_view(['GET'])
#@permission_classes([IsAdminUser])
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
    permission_classes = (IsAuthenticated,)

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


class SendFormEmail(View):
    
    def  get(self, request):

        # Get the form data 
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Subject - Django Email Testing', 
            'Hello ' + name + ',\n' + message, 
            'sender@example.com', # Admin
            [
                email,
            ]
        ) 

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('home') 

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

'''
from django.conf import settings

def send_html_email(to_list, subject, templates, context, sender=settings.DEFAULT_FROM_EMAIL):
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender)
    return msg.send()


def notify_subscribers(request):
    # emails = Subscriber.objects.all().values_list('email', flat=True)
    emails = 'saugatkafley@gmail.com'
    context = {
        'news': 'We have good news!'
    }
    
    res = send_html_email("saugatkafley@gmail.com", 'Good news', 'email_send.html', context, "volunteermanagementsoftware@gmail.com")
    if (res ==1):
        return HttpResponse("Message sent")
    else:
        return HttpResponse("Message  not sent")

import os
def send_mail(request):
    subject = "Email Message."
    from_email = settings.EMAIL_HOST_USER
    to_email =["saugatkafley@gmail.com"]
    # os.path.join(settings.BASE_DIR, 'templates/email_send')
    with open(os.path.join(settings.BASE_DIR, 'templates\email_send.txt')) as f:
        message = f.read()
    # with open(settings.BASE_DIR + os.path.join(settings.BASE_DIR,'templates/email_send.txt') )as f:
    #     message = f.read()
    mes = EmailMultiAlternatives(subject= subject, body =message, from_email = from_email, to_email = [to_email])
    html_template = get_template("tempaltes/email_send.html").render()
    mes.attach_alternative(html_template,"text/html")
    mes.send()

'''