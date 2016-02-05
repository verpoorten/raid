# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raidmosan', '0003_auto_20160205_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='categorie',
            field=models.CharField(choices=[('DAMES', 'Dames'), ('HOMMES', 'Hommes'), ('MIXTE', 'Mixte')], max_length=6, error_messages={'required': 'Catégorie obligatoire'}),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='nom_equipe',
            field=models.CharField(max_length=100, unique=True, error_messages={'unique': "Ce nom d'équipe existe déjà."}),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='nom_participant_1',
            field=models.CharField(max_length=50, error_messages={'required': 'Nom du participant 1 obligatoire'}),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='nom_participant_2',
            field=models.CharField(max_length=50, error_messages={'required': 'Nom du participant 2 obligatoire'}),
        ),
    ]
