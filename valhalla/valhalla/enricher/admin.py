from django.contrib import admin

from .models import Enricher


# Register your models here.
class EnricherAdmin(admin.ModelAdmin):
    list_display = ["id", "scan_id", "uuid", "power", "scope", "tasks", "completion", "status"]


admin.site.register(Enricher, EnricherAdmin)
