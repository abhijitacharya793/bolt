from rest_framework.viewsets import ModelViewSet

from api.models import Api
from api.serializers import ApiSerializer


class ApiModelViewSet(ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
