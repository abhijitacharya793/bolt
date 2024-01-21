from django.contrib import admin

from .models import Risk, Tag, Vulnerability


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class RiskAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "abbreviation"]


class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "risk", "severity", "power"]


admin.site.register(Tag, TagAdmin)
admin.site.register(Risk, RiskAdmin)
admin.site.register(Vulnerability, VulnerabilityAdmin)
