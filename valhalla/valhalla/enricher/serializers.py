from rest_framework import serializers

from .models import Enricher


class EnricherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enricher
        fields = '__all__'
