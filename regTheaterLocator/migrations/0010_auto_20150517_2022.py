# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0009_auto_20150517_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='production',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='production',
            name='closes',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='opens',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='time',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
