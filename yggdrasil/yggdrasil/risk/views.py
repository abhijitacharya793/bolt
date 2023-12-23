from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Risk, Vulnerability, Tag, Script, Workflow
from .serializers import RiskSerializer, VulnerabilitySerializer, TagSerializer, ScriptSerializer, WorkflowSerializer


class TagModelViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RiskModelViewSet(ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer


class ScriptModelViewSet(ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer

    def get_queryset(self):
        script_id = self.request.query_params.get('script_id')
        if script_id is not None:
            queryset = Script.objects.filter(id=script_id)
        else:
            queryset = Script.objects.all()
        return queryset


class WorkflowModelViewSet(ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer

    def get_queryset(self):
        root = self.request.query_params.get('root')
        workflow_id = self.request.query_params.get('workflow_id')
        vulnerability_id = self.request.query_params.get('vulnerability_id')
        if workflow_id is not None:
            if root == "True":
                print("Root flow")
                queryset = Workflow.objects.filter(vulnerability__id=vulnerability_id, previous_workflows=None)
            else:
                print("normal flow")
                queryset = Workflow.objects.filter(vulnerability__id=vulnerability_id, previous_workflows=workflow_id)
        else:
            print("Default")
            queryset = Workflow.objects.all()
        return queryset


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
