# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0010_auto_20150517_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='creation_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
