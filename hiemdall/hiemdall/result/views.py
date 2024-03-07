from rest_framework.viewsets import ModelViewSet

from .models import Result
from .serializers import ResultSerializer


class ResultModelViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        scan_id = self.request.query_params.get('scan_id')
        if scan_id is not None:
            queryset = Result.objects.filter(scan_id=scan_id)
        else:
            queryset = Result.objects.all()
        return queryset
