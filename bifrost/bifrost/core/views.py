from rest_framework.viewsets import ModelViewSet

from .models import Finding, Host
from .serializers import FindingSerializer, HostSerializer


class FindingModelViewSet(ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer


class HostModelViewSet(ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
