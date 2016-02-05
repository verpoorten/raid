# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raidmosan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='nom_equipe',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
