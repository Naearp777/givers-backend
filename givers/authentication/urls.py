from django.conf.urls import include
from django.urls import path,include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('api/users/login/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/users/profile/',views.getUserProfile,name='user-profile'),
    #path('api/users/',views.getUsers,name='all_users'),
    #path('api/users/register/',views.registerUser,name='register'),
    #path('api/users/changepassword/',views.ChangePasswordView,name='change_password'),
    #path('api/password_reset/',include('django_rest_passwordreset.urls'),name='reset_password'),
]