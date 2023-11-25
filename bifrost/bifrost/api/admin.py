from django.contrib import admin

from api.models import Api, Header, Query


class ApiAdmin(admin.ModelAdmin):
    pass


class QueryAdmin(admin.ModelAdmin):
    pass


class HeaderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Api, ApiAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(Header, HeaderAdmin)
