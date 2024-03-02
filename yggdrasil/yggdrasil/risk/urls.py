from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'tag', views.TagModelViewSet, basename='tag')
router.register(r'fuzzing', views.FuzzingModelViewSet, basename='fuzzing')
router.register(r'risk', views.RiskModelViewSet, basename='risk')
router.register(r'vulnerability', views.VulnerabilityModelViewSet, basename='vulnerability')
router.register(r'template', views.TemplateModelViewSet, basename='template')
urlpatterns = [] + router.urls
