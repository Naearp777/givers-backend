from django.conf.urls import include
from django.urls import path, include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='user-profile'),
    path('', views.getUsers, name='all_users'),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
]
