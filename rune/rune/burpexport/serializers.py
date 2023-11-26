from rest_framework import serializers

from .models import BurpExport


class BurpExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BurpExport
        fields = ['name', 'scope', 'power', 'burpExport']
