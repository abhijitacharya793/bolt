from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'tag', views.TagModelViewSet, basename='tag')
router.register(r'risk', views.RiskModelViewSet, basename='risk')
router.register(r'vulnerability', views.VulnerabilityModelViewSet, basename='vulnerability')
urlpatterns = [] + router.urls
