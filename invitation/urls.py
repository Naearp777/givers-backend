from django.urls import path
from .import views


urlpatterns = [

    path('<int:U_id>/<int:E_id>/', views.invite, name='invite'),
    path('<int:U_id>/', views.invite_display_id, name='invitation'),
    path('read/<int:I_id>/',
         views.invite_display_id_read, name='invitation_read'),

]
