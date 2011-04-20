from django.shortcuts import render

from ssb import models


def list(request):
    sessions = models.SystemSession.objects.all()
    return render(request, "list.html", {"sessions": sessions})
