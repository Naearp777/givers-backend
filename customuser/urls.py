from django.urls import path
from .import views

urlpatterns=[

    path('api/register/user/',views.registerUser,name='register_user'),
    path('api/user/update/<int:pk>/',views.UserUpdate.as_view(),name='update_user'),
    

]