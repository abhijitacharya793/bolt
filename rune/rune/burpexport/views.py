from rest_framework.viewsets import ModelViewSet

from .models import BurpExport
from .serializers import BurpExportSerializer


class BurpExportModelViewSet(ModelViewSet):
    queryset = BurpExport.objects.all()
    serializer_class = BurpExportSerializer
