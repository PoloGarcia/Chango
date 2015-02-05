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
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

# Chango imports
import settings
import models


def all_render_view(request):
    pass


def detail_render_view(request, chango_id):
    pass