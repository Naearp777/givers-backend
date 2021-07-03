#from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from customuser.models  import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    isAdmin = serializers.SerializerMethodField(read_only = True)

    class Meta :
        model = User
        fields ='__all__'

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','email','full_name','token', 'volunteer', 'organization']

    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    class Meta:
        model = User
        fields = ['token']

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)


from django.contrib.auth.tokens  import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,  urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    # redirect_url = serializers.CharField(max_length=500, required=False)
    class Meta:
        fields = ['email']
'''
    def validate(self,attrs):
        email = attrs['data'].get('email','')
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            uidb64 = urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user)

            subject = "Greetings from Givers!"
            current_site = get_current_site(
                request = attrs['data'].get('request')).domain
            relativeLink = reverse('password_reset_confirm', kwargs={'uidb64':uidb64, 'token':token})
            absurl = 'http://' + current_site + relativeLink 
            email_body = 'Hi' + user.full_name+ 'Use this Link below to verify your email\n'
            send_mail(subject,email_body,settings.EMAIL_HOST_USER, [user.email])

        return super().validate(attrs)
'''