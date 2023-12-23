from rest_framework.viewsets import ModelViewSet

from .models import Finding
from .serializers import FindingSerializer


class FindingModelViewSet(ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
