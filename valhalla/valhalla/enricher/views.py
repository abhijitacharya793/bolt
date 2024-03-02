from rest_framework.viewsets import ModelViewSet

from .models import Enricher
from .serializers import EnricherSerializer


class EnricherModelViewSet(ModelViewSet):
    queryset = Enricher.objects.all()
    serializer_class = EnricherSerializer

    def get_queryset(self):
        triggered = self.request.query_params.get('triggered')
        scan_id = self.request.query_params.get('scan_id')
        if triggered is not None:
            queryset = Enricher.objects.filter(triggered=triggered)
        elif scan_id is not None:
            queryset = Enricher.objects.filter(scan_id=scan_id)
        else:
            queryset = Enricher.objects.all()
        return queryset
