from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'query', views.QueryModelViewSet, basename='api_query')
router.register(r'header', views.HeaderModelViewSet, basename='api_header')
router.register(r'', views.ApiModelViewSet, basename='api')
urlpatterns = [] + router.urls
