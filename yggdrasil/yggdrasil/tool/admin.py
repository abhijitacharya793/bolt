from django.contrib import admin

from .models import Tool


# Register your models here.
class ToolAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tool, ToolAdmin)
