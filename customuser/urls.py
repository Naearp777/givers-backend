from django.urls import path
from .import views

urlpatterns=[

    path('api/register/user/',views.registerUser,name='register_user'),
    path('api/register/verify/<int:id>/<int:otp>/',views.RegisterVerify,name='register_verify'),
    path('api/register/verify/resend/<int:id>/',views.Resend_otp,name='resend_otp'),
    path('api/user/update/<int:pk>/',views.UserUpdate.as_view(),name='update_user'),
]