from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls

admin.site.site_header = "Givers"
admin.site.site_title = "Givers"
admin.site.index_title = "Welcome to Givers"

# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/user/', include("customuser.urls")),
    path('api/events/', include("events.urls"), name="events"),
    path('api/users/', include("authentication.urls")),
    path('api/volunteer/', include("volunteer.urls")),
    path('api/organization/', include("organization.urls")),
    path('api/validate/', include("validators.urls")),
    path('api/category/', include("category.urls")),
    path('api/miscellaneous/', include("miscellaneous.urls")),
    path('api/verification/', include("verify.urls")),
    path('api/invite/', include("invitation.urls")),

    path('docs/', include_docs_urls(title='Todo Api')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)