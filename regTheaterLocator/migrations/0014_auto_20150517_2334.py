# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0013_auto_20150517_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='closes',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='opens',
            field=models.DateField(null=True),
        ),
    ]
