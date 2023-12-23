from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'', views.FindingModelViewSet, basename='finding')
urlpatterns = [] + router.urls
