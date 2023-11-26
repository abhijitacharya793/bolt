from celery import shared_task
from django.db import models

POWER = [("l", "low"), ("m", "medium"), ("h", "high"), ]


@shared_task
def parse_burp_export():
    print("PARSING BURPSUITE EXPORT")
    return


class BurpExport(models.Model):
    name = models.CharField(max_length=100)
    scope = models.CharField(max_length=500, null=True, blank=True)
    power = models.CharField(max_length=1, choices=POWER)
    burpExport = models.FileField(upload_to="media/burpExport/")

    def __str__(self):
        return f"{self.name}: {self.power}"

    def save(self, *args, **kwargs):
        super(BurpExport, self).save(*args, **kwargs)
        # Call parsing task
        parse_burp_export.delay()
