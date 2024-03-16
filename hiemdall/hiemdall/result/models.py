from django.db import models


class Result(models.Model):
    scan_id = models.IntegerField()
    vulnerability_id = models.IntegerField()
    uuid = models.CharField(max_length=100, null=True, blank=True)
    template_id = models.CharField(max_length=100, null=True, blank=True)
    payload_str = models.CharField(max_length=1000, null=True, blank=True)
    matched_at = models.CharField(max_length=1000, null=True, blank=True)
    curl_command = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.scan_id} - {self.template_id}"
