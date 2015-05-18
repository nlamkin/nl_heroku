# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0003_auto_20150514_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theater',
            name='style',
        ),
    ]
