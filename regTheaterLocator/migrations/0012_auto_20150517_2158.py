# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0011_auto_20150517_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='opens',
        ),
        migrations.AddField(
            model_name='performance',
            name='opens',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='production',
            name='closes',
            field=models.DateTimeField(null=True),
        ),
    ]
