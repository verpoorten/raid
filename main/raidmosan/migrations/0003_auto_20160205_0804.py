# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raidmosan', '0002_auto_20160204_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='nom_equipe',
            field=models.CharField(max_length=100, unique=True, error_messages={'unique': 'This email has already been registered.'}),
        ),
    ]
