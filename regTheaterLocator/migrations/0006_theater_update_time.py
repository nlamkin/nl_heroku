# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0005_auto_20150515_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='update_time',
            field=models.DateTimeField(null=True),
        ),
    ]
