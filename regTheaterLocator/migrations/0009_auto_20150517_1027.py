# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0008_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
