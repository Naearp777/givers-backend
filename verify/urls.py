from django.urls import path
from .import views

urlpatterns = [

    path('api/verification/user/<int:U_id>/',
         views.verification, name='verification'),
    path('api/verification/alluser/',
         views.showverifyrequest, name='all_verify_list'),
    path('api/showalluser/', views.showalluser, name="show_all_user"),
    path('api/showspecificuser/<int:U_id>/', views.showspecificrequest,
         name="show_specific_user"),
    path('api/showallvolunteers/', views.showallvolunteer,
         name="show_all_volunteer"),
]
