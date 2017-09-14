# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_auto_20161228_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacte',
            name='mail',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='contacte',
            name='message',
            field=models.TextField(null=True, blank=True),
        ),
    ]
