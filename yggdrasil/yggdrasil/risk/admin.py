from django.contrib import admin

from .models import Risk, Tag, Script, Workflow, Vulnerability


class TagAdmin(admin.ModelAdmin):
    pass


class RiskAdmin(admin.ModelAdmin):
    pass


class ScriptAdmin(admin.ModelAdmin):
    pass


class WorkflowAdmin(admin.ModelAdmin):
    pass


class VulnerabilityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Risk, RiskAdmin)
admin.site.register(Script, ScriptAdmin)
admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(Vulnerability, VulnerabilityAdmin)
