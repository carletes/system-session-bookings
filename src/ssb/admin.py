from django.contrib import admin

from ssb import models


class SystemSessionAdmin(admin.ModelAdmin):
    
    list_display = ("title", "start_date", "status")
    list_filter = ("status",)
    search_fields = ("title", "description")
    date_hierarchy = "start_date"


admin.site.register(models.SystemSession, SystemSessionAdmin)
