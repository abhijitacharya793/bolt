import uuid as uid

from django.db import models


# This model will store the actual API to Vulnerability ID mapping from yggdrasil
class Finding(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uid.uuid4, editable=False)
    api = models.ForeignKey('api.Api', on_delete=models.CASCADE)

    # vulnerability = models.ForeignKey

    def __str__(self):
        return self.api.name


class Host(models.Model):
    root_domain = models.CharField(max_length=500)
    host = models.CharField(max_length=500)
    ip = models.CharField(max_length=50)
    status_code = models.CharField(max_length=5)

    def __str__(self):
        return self.host
