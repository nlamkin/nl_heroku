# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0007_auto_20150515_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=8)),
                ('production', models.ForeignKey(to='regTheaterLocator.Production')),
            ],
        ),
    ]
