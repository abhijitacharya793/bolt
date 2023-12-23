from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Api, Query, Header
from .serializers import ApiSerializer, QuerySerializer, HeaderSerializer


class QueryModelViewSet(ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def get_queryset(self):
        uuid = self.request.query_params.get('uuid')
        if uuid is not None:
            queryset = Query.objects.filter(api=uuid)
        else:
            queryset = Query.objects.all()
        return queryset


class HeaderModelViewSet(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

    def get_queryset(self):
        uuid = self.request.query_params.get('uuid')
        if uuid is not None:
            queryset = Header.objects.filter(api=uuid)
        else:
            queryset = Header.objects.all()
        return queryset


class ApiModelViewSet(ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

    def get_queryset(self):
        uuid = self.request.query_params.get('uuid')
        if uuid is not None:
            queryset = Api.objects.filter(uuid=uuid)
        else:
            queryset = Api.objects.all()
        return queryset
