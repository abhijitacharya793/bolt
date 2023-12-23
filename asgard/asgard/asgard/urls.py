from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from api import views

schema_view = get_schema_view(
    openapi.Info(
        title="asgard",
        default_version='v1',
        description="Service to manage scheduled scans",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@asgard.bolt"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('asgard/v1/admin/', admin.site.urls),
    # path('asgard/v1/core/', include('core.urls')),
    path('asgard/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('asgard/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('asgard/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
