from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Risk, Vulnerability, Tag
from .serializers import *


class TagModelViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RiskModelViewSet(ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


class VulnerabilityModelViewSet(ModelViewSet):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer

    def get_queryset(self):
        vulnerability_id = self.request.query_params.get('vulnerability_id')
        if vulnerability_id is not None:
            queryset = Vulnerability.objects.filter(id=vulnerability_id)
        else:
            queryset = Vulnerability.objects.all()
        return queryset


class TemplateModelViewSet(ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def get_queryset(self):
        vulnerability_id = self.request.query_params.get('vulnerability_id')
        if vulnerability_id is not None:
            queryset = Template.objects.filter(vulnerability__id=vulnerability_id)
        else:
            queryset = Template.objects.all()
        return queryset
