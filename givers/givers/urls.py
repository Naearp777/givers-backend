from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from djano.auth.contrib
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("customuser.urls")),
    path('',include("events.urls")),
    path('',include("authentication.urls")),
    path('',include("volunteer.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

