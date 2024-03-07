from django.contrib import admin

from .models import Result


# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display = ["id", "scan_id"]


admin.site.register(Result, ResultAdmin)
