import uuid as uid

from django.db import models


class Api(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uid.uuid4, editable=False)
    target = models.CharField(max_length=100)
    root_domain = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    protocol = models.CharField(max_length=10, default="http")
    protocol_version = models.CharField(max_length=10, default="HTTP/1.1")
    port = models.IntegerField(default=80)
    method = models.CharField(max_length=100)  # TODO: Choices
    path = models.CharField(max_length=100)
    body = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.method} : {self.target}{self.path}"

    @property
    def api_string(self):
        api_string = f"{self.method} {self.path}?"
        # ADD QUERY PARAM
        for query_param in self.query_object:
            api_string += f"{query_param['name']}={query_param['value']}&"
        api_string += " HTTP/1.1\n"
        for header in self.header_object:
            api_string += f"{header['name']}: {header['value']}\n"
        if self.method == "POST" or self.method == "PUT":
            api_string += f"\n\n{self.body}"
        return api_string


class Query(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=100)
    api = models.ForeignKey(Api, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} : {self.value}"


class Header(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=5000)
    api = models.ForeignKey(Api, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} : {self.value}"
