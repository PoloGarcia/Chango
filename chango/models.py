from django.db import models
from django.utils import timezone
import datetime


class Chango(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    geo_location = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self): 
        return self.name