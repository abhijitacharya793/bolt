from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path('bifrost/v1/admin/', admin.site.urls),
    path('bifrost/v1/api/', include('api.urls'))
]
