from rest_framework import serializers

from api.models import Api


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ['protocol', 'port', 'method', 'path', 'query_param', 'header', 'body', 'target', 'domain',
                  'root_domain']
