# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nom_equipe', models.CharField(max_length=100)),
                ('nom_participant_1', models.CharField(max_length=50)),
                ('nom_participant_2', models.CharField(max_length=50)),
                ('categorie', models.CharField(max_length=6, choices=[('DAMES', 'Dames'), ('HOMMES', 'Hommes'), ('MIXTE', 'Mixte')])),
                ('responsable_email', models.EmailField(max_length=254)),
                ('responsable_telephone', models.CharField(max_length=30)),
                ('challenge_raid_trophy', models.BooleanField(default=False)),
                ('taille_t_shirt', models.CharField(max_length=6, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra large')])),
                ('reglement_ok', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nom_equipe'],
            },
        ),
    ]
