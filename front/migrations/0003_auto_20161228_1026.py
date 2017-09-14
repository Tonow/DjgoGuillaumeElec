# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20161228_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacte',
            old_name='numero_voie',
            new_name='numero_de_la_voie',
        ),
    ]
