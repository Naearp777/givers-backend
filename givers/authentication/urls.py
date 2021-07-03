from django.conf.urls import include, url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from django.views.generic import TemplateView
urlpatterns = [
    path('api/users/login/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/profile/',views.getUserProfile,name='user-profile'),
    path('api/users/',views.getUsers,name='all_users'),
    path('api/users/register/',views.registerUser,name='register'),
   
    # path('api/users/change_password/',views.ChangePasswordView.as_view(),name='change_password'),
    # path('api/password_reset/',auth_views.password_reset, name='password_reset'),
    # path('api/password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # path('api/reset/done',auth_views.password_reset_complete, name='password_reset_complete')
    path('api/password_reset/',include('django_rest_passwordreset.urls'),name='reset_password'),
   

]
'''

urlpatterns += [
    path('template/home', TemplateView.as_view(template_name="home.html"), name='home'),
    path('send_mail/', views.my_mail, )
]

urlpatterns += [
# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),

]
'''

urlpatterns += [
    path('password_reset/<uidb64>/<token>/', views.PasswordTokenCheckAPI.as_view(), name ='password_reset_confirm'),
    path('request_reset_email/',views.RequestPasswordResetEmail.as_view(), name ='request_reset_email')
]
