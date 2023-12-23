from django.contrib import admin

from .models import Enricher


# Register your models here.
class EnricherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Enricher, EnricherAdmin)
