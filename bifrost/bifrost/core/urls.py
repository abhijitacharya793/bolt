from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'finding', views.FindingModelViewSet, basename='finding')
router.register(r'host', views.HostModelViewSet, basename='host')
urlpatterns = [] + router.urls
