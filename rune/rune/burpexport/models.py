from celery import shared_task
from django.db import models

from .helper import parse_xml, parse_api, save_api, enrich_scan

POWER = [(1, "low"), (2, "medium"), (3, "high"), ]


@shared_task
def parse_burp_export(burp_export, name, scope, power, completion):
    print(f"PARSING BURPSUITE EXPORT for: {name} for scope {scope}")
    api_strings = parse_xml(burp_export)
    for api_string in api_strings:
        api = parse_api(api_string)
        api_id = save_api(api, scope)
        if api_id != -1:
            enrich_scan(api_id, name, power)
    return


class BurpExport(models.Model):
    name = models.CharField(max_length=100)
    scope = models.CharField(max_length=500, null=True, blank=True)
    power = models.IntegerField(choices=POWER)
    completion = models.IntegerField(default=0)
    burpExport = models.FileField(upload_to="burpExport/")

    def __str__(self):
        return f"{self.name}: {self.power}"

    def save(self, *args, **kwargs):
        super(BurpExport, self).save(*args, **kwargs)
        # Call parsing task
        parse_burp_export.apply_async(
            args=['media/' + self.burpExport.name, self.name, self.scope, self.power, self.completion])
