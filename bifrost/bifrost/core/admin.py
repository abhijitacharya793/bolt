from django.contrib import admin

from .models import Finding


class FindingAdmin(admin.ModelAdmin):
    list_display = ["uuid", "api"]


admin.site.register(Finding, FindingAdmin)
