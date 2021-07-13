from django.urls import path
from .import views

urlpatterns=[

    path('api/validate/username/<str:username>',views.validateusername,name='validate_username'),
    path('api/validate/email/<str:email>',views.validateemail,name='validate_email'),

]