# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_auto_20161228_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacte',
            name='telephone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Veuiller donner un téléphone valide', code='Invalid number', regex='^\\d{10}$')]),
        ),
    ]
