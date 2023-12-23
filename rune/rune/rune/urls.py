from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="rune",
        default_version='v1',
        description="Service to manage input triggers like burp export, mitmproxy or burp live traffic.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@rune.bolt"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('rune/v1/admin/', admin.site.urls),
    path('rune/v1/burpExport/', include('burpexport.urls')),
    path('rune/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('rune/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('rune/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)