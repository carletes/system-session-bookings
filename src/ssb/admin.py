from django.contrib import admin

from ssb import models


class SystemSessionAdmin(admin.ModelAdmin):
    
    list_display = ("title", "start_date", "status")
    list_filter = ("status",)
    search_fields = ("title", "description")
    date_hierarchy = "start_date"
    actions = ("approve_sessions", "cancel_sessions")

    def approve_sessions(self, request, queryset):
        queryset.update(status="approved")
    approve_sessions.short_description = "Approve system sessions"

    def cancel_sessions(self, request, queryset):
        queryset.update(status="canceled")
    cancel_sessions.short_description = "Cancel system sessions"

    def get_actions(self, request):
        actions = super(SystemSessionAdmin, self).get_actions(request)
        if not request.user.has_perm("ssb.can_change_status"):
            del actions["approve_sessions"]
            del actions["cancel_sessions"]
        return actions


admin.site.register(models.SystemSession, SystemSessionAdmin)
