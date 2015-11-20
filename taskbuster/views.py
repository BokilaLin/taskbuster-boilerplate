# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render
from django.template import RequestContext
from django.utils.timezone import now

def home(request):
    today = datetime.date.today()
    context = RequestContext(request)
    context['today'] = today
    context['now'] = now()
    return render(request, "taskbuster/index.html", context)

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
