from django.contrib import admin

from service_app.models import Printer, Check


class CheckAdmin(admin.ModelAdmin):
    list_display = ('printer', 'type', 'status')

    list_filter = ('printer', 'type', 'status')


class PrinterAdmin(admin.ModelAdmin):
    list_display = ('name', 'point_id', 'api_key')

    list_filter = ('name', 'point_id', 'api_key')


admin.site.register(Check, CheckAdmin)
admin.site.register(Printer, PrinterAdmin)
