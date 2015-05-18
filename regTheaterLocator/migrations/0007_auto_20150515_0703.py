# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0006_theater_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='admin',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, related_name='theater_admin', null=True),
        ),
        migrations.AlterField(
            model_name='theater',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
