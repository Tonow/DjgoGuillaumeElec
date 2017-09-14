# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20161228_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacte',
            name='code_postal',
            field=models.IntegerField(max_length=6, validators=[django.core.validators.RegexValidator(regex='^\\d{6}$', message='Veuiller donner un code postal valide', code='Invalid postal')]),
        ),
        migrations.AlterField(
            model_name='contacte',
            name='telephone',
            field=models.FloatField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$', message='Veuiller donner un téléphone valide', code='Invalid number')]),
        ),
    ]
