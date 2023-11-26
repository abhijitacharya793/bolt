from django.contrib import admin

from .models import BurpExport


# Register your models here.
class BurpExportAdmin(admin.ModelAdmin):
    pass


admin.site.register(BurpExport, BurpExportAdmin)
