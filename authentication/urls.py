from django.conf.urls import include
from django.urls import path, include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('api/users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/users/profile/', views.getUserProfile, name='user-profile'),
    path('api/users/', views.getUsers, name='all_users'),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('api/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
]
