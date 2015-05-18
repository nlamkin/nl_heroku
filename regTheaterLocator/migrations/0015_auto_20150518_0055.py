# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0014_auto_20150517_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='closes',
            field=models.CharField(null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='production',
            name='opens',
            field=models.CharField(null=True, max_length=10),
        ),
    ]
