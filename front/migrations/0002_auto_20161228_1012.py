# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacte',
            old_name='sender',
            new_name='mail',
        ),
        migrations.AddField(
            model_name='contacte',
            name='code_postal',
            field=models.PositiveIntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacte',
            name='numero_voie',
            field=models.PositiveIntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacte',
            name='rue',
            field=models.CharField(default=-1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacte',
            name='ville',
            field=models.CharField(default=-1, max_length=90),
            preserve_default=False,
        ),
    ]
