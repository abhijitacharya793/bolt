from django.db import models


# from .helper import parse_xml, parse_api, save_api, enrich_scan

# POWER = [(1, "low"), (2, "medium"), (3, "high"), ]


class Enricher(models.Model):
    name = models.CharField(max_length=100)
    uuid = models.CharField(max_length=100)
    power = models.IntegerField()
    scans = models.CharField(max_length=1000, null=True, blank=True)
    triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.power}"

    def save(self, *args, **kwargs):
        super(Enricher, self).save(*args, **kwargs)
        # Get all vulnerabilities from yggdrasil

        # Enrich scan type and save
