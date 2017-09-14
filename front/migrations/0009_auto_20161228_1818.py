# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_auto_20161228_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacte',
            name='code_postal',
            field=models.IntegerField(max_length=5, validators=[django.core.validators.RegexValidator(regex='^\\d{5}$', message='Veuiller donner un code postal valide', code='Invalid postal')]),
        ),
    ]
