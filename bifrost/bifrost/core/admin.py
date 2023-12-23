from django.contrib import admin

from .models import Finding


class FindingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Finding, FindingAdmin)
