from django.urls import path
from .import views

urlpatterns = [

    path('username/<str:username>',
         views.validateusername, name='validate_username'),
    path('email/<str:email>',
         views.validateemail, name='validate_email'),

]
