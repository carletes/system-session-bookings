from django.shortcuts import render_to_response
from django.template import RequestContext

from ssb import models


def list(request):
    sessions = models.SystemSession.objects.all()
    return render_to_response("list.html",
                              {"sessions": sessions},
                              context_instance=RequestContext(request))
