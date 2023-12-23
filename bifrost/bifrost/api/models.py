import uuid as uid

from django.db import models


class Api(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uid.uuid4, editable=False)
    target = models.CharField(max_length=100)
    root_domain = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    protocol = models.CharField(max_length=10, default="http")
    port = models.IntegerField(default=80)
    method = models.CharField(max_length=100)  # TODO: Choices
    path = models.CharField(max_length=100)
    body = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.method} : {self.target}{self.path}"

    @property
    def api_string(self):
        return f"{self.target}"


class Query(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=100)
    api = models.ForeignKey(Api, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} : {self.value}"


class Header(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=200)
    api = models.ForeignKey(Api, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} : {self.value}"
