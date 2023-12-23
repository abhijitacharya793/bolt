from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Tool
from .serializers import ToolSerializer


class ToolModelViewSet(ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
