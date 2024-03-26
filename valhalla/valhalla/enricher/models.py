from django.db import models

from .helper import get_api_details, enrich_api, get_risk_details

# from .helper import parse_xml, parse_api, save_api, enrich_scan

POWER = [(1, "low"), (2, "medium"), (3, "high"), ]


class Enricher(models.Model):
    scan_id = models.IntegerField()
    uuid = models.CharField(max_length=100)
    power = models.IntegerField(choices=POWER)
    scope = models.CharField(max_length=500, null=True, blank=True)
    tasks = models.CharField(max_length=1000, null=True, blank=True)
    completion = models.IntegerField(default=0)
    triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.scan_id}: {self.power}"

    def save(self, *args, **kwargs):
        api = get_api_details(self.uuid)
        # Get all vulnerabilities from yggdrasil
        risks = get_risk_details()
        # Enrich scan type and save
        self.tasks = enrich_api(api, risks)
        super(Enricher, self).save(*args, **kwargs)
