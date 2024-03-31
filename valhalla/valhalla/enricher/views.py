from rest_framework.viewsets import ModelViewSet

from .models import Enricher
from .serializers import EnricherSerializer


class EnricherModelViewSet(ModelViewSet):
    queryset = Enricher.objects.all()
    serializer_class = EnricherSerializer

    def get_queryset(self):
        status = self.request.query_params.get('status')
        scan_id = self.request.query_params.get('scan_id')
        if status is not None:
            queryset = Enricher.objects.filter(status=status)
        elif scan_id is not None:
            queryset = Enricher.objects.filter(scan_id=scan_id)
        else:
            queryset = Enricher.objects.all()
        return queryset
