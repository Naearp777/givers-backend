from django.urls import path
from .import views

urlpatterns = [
    path('register/user/', views.registerUser, name='register_user'),
    path('register/verify/<int:id>/<int:otp>/',
         views.RegisterVerify, name='register_verify'),
    path('register/verify/resend/<int:id>/',
         views.Resend_otp, name='resend_otp'),
    path('update/<int:pk>/',
         views.UserUpdate.as_view(), name='update_user'),
    path('profile/<int:U_id>/',
         views.get_User_Profile, name='get_user_profile'),
]
