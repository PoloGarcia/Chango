# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chango',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.CharField(max_length=400, verbose_name='Descripci\xf3n')),
                ('geo_location', models.CharField(max_length=50, verbose_name='Ubicaci\xf3n Geogr\xe1fica')),
                ('pub_date', models.DateTimeField(verbose_name='Fecha de Publicaci\xf3n')),
            ],
            options={
                'verbose_name': 'Chango',
                'verbose_name_plural': 'Changos',
            },
            bases=(models.Model,),
        ),
    ]
