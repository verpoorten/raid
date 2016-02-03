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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nom_equipe', models.CharField(max_length=100)),
                ('nom_participant_1', models.CharField(max_length=50)),
                ('nom_participant_2', models.CharField(max_length=50)),
                ('categorie', models.CharField(choices=[('DAMES', 'Dames'), ('HOMMES', 'Hommes'), ('MIXTE', 'Mixte')], max_length=6)),
                ('responsable_email', models.EmailField(max_length=254)),
                ('responsable_telephone', models.CharField(max_length=30)),
                ('challenge_raid_trophy', models.BooleanField(default=False)),
                ('taille_t_shirt_1', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra large')], max_length=6)),
                ('taille_t_shirt_2', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra large')], max_length=6)),
                ('reglement_ok', models.BooleanField(default=False)),
                ('inscription_validee', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nom_equipe'],
            },
        ),
    ]
