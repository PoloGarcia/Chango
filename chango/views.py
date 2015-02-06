#coding:utf-8

# Python imports
import os
import datetime

# Django imports
import django.core.exceptions
import django.core.servers.basehttp
import django.core.urlresolvers
import django.core.paginator
import django.contrib.auth
import django.contrib.auth.forms
import django.core.mail
import django.http
import django.shortcuts
import django.utils.encoding
import django.template.context
import django.contrib.auth.models
from django.contrib import messages

# Chango imports
import models


def all_render_view(request):

    template_variables = {}
    changos = models.Chango.objects.all().order_by('-name')

    template_variables['changos'] = changos

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        "sections/all.html",
        template_context
    )


def detail_render_view(request, chango_id):

    template_variables = {}

    try:
        chango = models.Chango.objects.get(pk=chango_id)
        template_variables['chango'] = chango

    except models.Chango.DoesNotExist as e:
        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        "sections/detail.html",
        template_context
    )