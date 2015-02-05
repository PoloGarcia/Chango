#coding:utf-8

from django.db import models
from django.utils import timezone
import datetime


class Chango(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Nombre")
    description = models.CharField(max_length=400, verbose_name=u"Descripción")
    geo_location = models.CharField(max_length=50, verbose_name=u"Ubicación Geográfica")
    pub_date = models.DateTimeField(verbose_name=u"Fecha de Publicación")

    class Meta:
        verbose_name = u"Chango"
        verbose_name_plural = u"Changos"

    def __unicode__(self):
        return self.name