from django.contrib import admin

from .models import Api, Header, Query


class ApiAdmin(admin.ModelAdmin):
    list_display = ["uuid", "target", "root_domain", "domain", "protocol", "protocol_version", "port", "method", "path"]


class QueryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "value", "api"]


class HeaderAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "value", "api"]


admin.site.register(Api, ApiAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(Header, HeaderAdmin)
