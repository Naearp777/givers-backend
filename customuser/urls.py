from django.urls import path
from .import views

urlpatterns=[

    path('api/register/user/',views.registerUser,name='register_user'),
    path('api/register/verify/<int:otp>/',views.RegisterVerify,name='register_verify'),
    

]