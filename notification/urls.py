from django.conf.urls import include
from django.urls import path
from . import views
import notifications.urls
# Create a list to create urls 

urlpatterns = [
    path('api/events/notification/', views.ShowNotifications, name = "show_notification"),
]


urlpatterns += [
    
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    
]
