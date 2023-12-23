import uuid as uid

from django.db import models


# This model will store the actual API to Vulnerability ID mapping from yggdrasil
class Finding(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uid.uuid4, editable=False)
    api = models.ForeignKey('api.Api', on_delete=models.CASCADE)
    # vulnerability = models.ForeignKey

    def __str__(self):
        return self.api.name
