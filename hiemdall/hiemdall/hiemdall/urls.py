from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="hiemdall",
        default_version='v1',
        description="Service to decide on the tasks to run for a particular API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@hiemdall.bolt"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('hiemdall/v1/admin/', admin.site.urls),
    path('hiemdall/v1/result/', include('result.urls')),
    path('hiemdall/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('hiemdall/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('hiemdall/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
