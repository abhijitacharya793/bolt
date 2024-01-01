from django.contrib import admin

from .models import Risk, Tag, Script, Workflow, Vulnerability


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class RiskAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "abbreviation"]


class ScriptAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "script"]


class WorkflowAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "script"]


class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "risk", "severity", "power", "workflows"]


admin.site.register(Tag, TagAdmin)
admin.site.register(Risk, RiskAdmin)
admin.site.register(Script, ScriptAdmin)
admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(Vulnerability, VulnerabilityAdmin)
