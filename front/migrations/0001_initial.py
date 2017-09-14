# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacte',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=80)),
                ('prenom', models.CharField(max_length=80)),
                ('message', models.TextField(null=True)),
                ('telephone', models.PositiveIntegerField()),
                ('sender', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(verbose_name='Date de la demende', auto_now_add=True)),
            ],
        ),
    ]
