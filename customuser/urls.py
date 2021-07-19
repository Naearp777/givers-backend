from django.urls import path
from .import views

urlpatterns=[

    path('api/register/user/',views.registerUser,name='register_user'),
    path('api/register/verify/<int:otp>/',views.RegisterVerify,name='register_verify'),
    path('api/register/verify/resend/<str:username>/',views.Resend_otp,name='resend_otp'),
    path('api/user/update/<int:pk>/',views.UserUpdate.as_view(),name='update_user'),
]