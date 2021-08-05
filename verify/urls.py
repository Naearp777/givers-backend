from django.urls import path
from .import views

urlpatterns = [

    path('api/verification/user/', views.verification, name='verification'),
   
]
