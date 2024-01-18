from django.contrib import admin

from .models import Finding, Host


class FindingAdmin(admin.ModelAdmin):
    list_display = ["uuid", "api"]


class HostAdmin(admin.ModelAdmin):
    list_display = ["root_domain", "host", "ip", "status_code"]


admin.site.register(Finding, FindingAdmin)

admin.site.register(Host, HostAdmin)
