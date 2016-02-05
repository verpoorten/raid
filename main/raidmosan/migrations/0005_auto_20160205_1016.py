# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raidmosan', '0004_auto_20160205_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='taille_t_shirt_1',
            field=models.CharField(error_messages={'required': 'Catégorie obligatoire'}, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra large')], max_length=6),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='taille_t_shirt_2',
            field=models.CharField(error_messages={'required': 'Catégorie obligatoire'}, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra large')], max_length=6),
        ),
    ]
