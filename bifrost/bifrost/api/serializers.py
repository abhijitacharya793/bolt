from rest_framework import serializers

from .models import Api, Query, Header


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = '__all__'
