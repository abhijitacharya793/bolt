from django.contrib import admin

from .models import BurpExport


# Register your models here.
class BurpExportAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "scope", "power", "burpExport"]


admin.site.register(BurpExport, BurpExportAdmin)
