from django.db import models


class Query(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} : {self.value}"


class Header(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} : {self.value}"


class Api(models.Model):
    protocol = models.CharField(max_length=10, default="http")
    port = models.IntegerField(default=80)
    method = models.CharField(max_length=100)  # TODO: Choices
    path = models.CharField(max_length=100)
    query_param = models.ForeignKey(Query, on_delete=models.CASCADE, blank=True, null=True)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, blank=True, null=True)
    body = models.CharField(max_length=1000, blank=True, null=True)
    target = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    root_domain = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.method} : {self.target}{self.path}"
