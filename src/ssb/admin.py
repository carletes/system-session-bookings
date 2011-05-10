import datetime

from django.contrib import admin
from django import forms
from django.forms import widgets

from ssb import models


def next_wednesday_10h():
    today = datetime.datetime.today()
    weekday = today.weekday()
    if weekday < 2:
        next_wed = today + datetime.timedelta(days=2 - weekday)
    else:
        next_wed  =today + datetime.timedelta(days=9 - weekday)
    return next_wed.replace(hour=10, minute=0, second=0)


class SystemSessionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs["initial"] = {"start_date": next_wednesday_10h()}
        forms.ModelForm.__init__(self, *args, **kwargs)

    class Meta:
        model = models.SystemSession
        widgets = {
            "impact_probability": widgets.RadioSelect,
            "impact_severity": widgets.RadioSelect,
        }


class SystemSessionAdmin(admin.ModelAdmin):
    
    actions = ("approve_sessions", "cancel_sessions")
    date_hierarchy = "start_date"
    form = SystemSessionForm
    list_display = ("title", "start_date", "approved")
    list_filter = ("approved",)
    search_fields = ("title", "purpose")

    def approve_sessions(self, request, queryset):
        queryset.update(approved=True)
    approve_sessions.short_description = "Approve system sessions"

    def cancel_sessions(self, request, queryset):
        queryset.update(approved=False)
    cancel_sessions.short_description = "Cancel system sessions"

    def get_actions(self, request):
        actions = super(SystemSessionAdmin, self).get_actions(request)
        if not request.user.has_perm("ssb.can_approve"):
            del actions["approve_sessions"]
            del actions["cancel_sessions"]
        return actions


admin.site.register(models.SystemSession, SystemSessionAdmin)
