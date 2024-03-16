from django.contrib import admin

from .models import Result


# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display = ["id", "scan_id", "vulnerability_id", "uuid", "template_id", "payload_str", "matched_at", "curl_command"]


admin.site.register(Result, ResultAdmin)
