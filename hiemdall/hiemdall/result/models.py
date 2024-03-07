from django.db import models


class Result(models.Model):
    scan_id = models.IntegerField()

    def __str__(self):
        return f"{self.scan_id}"
