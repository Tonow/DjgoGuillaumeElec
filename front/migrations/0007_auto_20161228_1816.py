# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_auto_20161228_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacte',
            name='telephone',
            field=models.TextField(max_length=10, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Veuiller donner un téléphone valide', regex='^\\d{10}$')]),
        ),
    ]
