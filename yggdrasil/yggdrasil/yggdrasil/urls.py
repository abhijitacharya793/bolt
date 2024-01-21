from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="yggdrasil",
        default_version='v1',
        description="Service to generate commands to run in ragnarok based on the power and scan type",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@yggdrasil.bolt"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('yggdrasil/v1/admin/', admin.site.urls),
    path('yggdrasil/v1/risk/', include('risk.urls')),
    path('yggdrasil/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('yggdrasil/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('yggdrasil/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
