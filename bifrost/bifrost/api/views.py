from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Api, Query, Header
from .serializers import ApiSerializer, QuerySerializer, HeaderSerializer


class QueryModelViewSet(ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class HeaderModelViewSet(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class ApiModelViewSet(ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
