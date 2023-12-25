from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="valhalla",
        default_version='v1',
        description="Service to decide on the tasks to run for a particular API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@valhalla.bolt"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('valhalla/v1/admin/', admin.site.urls),
    path('valhalla/v1/enricher/', include('enricher.urls')),
    path('valhalla/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('valhalla/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('valhalla/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
