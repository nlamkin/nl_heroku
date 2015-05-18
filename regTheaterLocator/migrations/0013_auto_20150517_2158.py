# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0012_auto_20150517_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performance',
            name='opens',
        ),
        migrations.AddField(
            model_name='production',
            name='opens',
            field=models.DateTimeField(null=True),
        ),
    ]
