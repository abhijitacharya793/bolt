from django.contrib import admin

from .models import *


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class RiskAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "abbreviation"]


class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "risk", "command", "severity", "power"]


class TemplateAdmin(admin.ModelAdmin):
    list_display = ["vulnerability", "path"]


admin.site.register(Tag, TagAdmin)
admin.site.register(Risk, RiskAdmin)
admin.site.register(Vulnerability, VulnerabilityAdmin)
admin.site.register(Template, TemplateAdmin)
