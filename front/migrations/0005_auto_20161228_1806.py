# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20161228_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacte',
            name='code_postal',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='contacte',
            name='telephone',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(regex='^\\d{10}$', code='Invalid number', message='Veuiller donner un téléphone valide')], max_length=10),
        ),
    ]
