from django.contrib import admin

from .models import Enricher


# Register your models here.
class EnricherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "uuid", "power", "tasks", "completion", "triggered"]


admin.site.register(Enricher, EnricherAdmin)
