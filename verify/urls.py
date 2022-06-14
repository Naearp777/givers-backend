from django.urls import path
from .import views

urlpatterns = [

    path('user/<int:U_id>/',
         views.verification, name='verification'),
    path('alluser/',
         views.showverifyrequest, name='all_verify_list'),
    path('showalluser/', views.showalluser, name="show_all_user"),
    path('showspecificuser/<int:U_id>/', views.showspecificrequest,
         name="show_specific_user"),
    path('showallvolunteers/', views.showallvolunteer,
         name="show_all_volunteer"),
]
