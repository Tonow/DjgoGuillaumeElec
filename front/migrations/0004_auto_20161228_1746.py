# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20161228_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacte',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
