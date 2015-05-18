# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0002_theater_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='show_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='production',
            name='update_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='updated_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='entry_updator'),
        ),
    ]
