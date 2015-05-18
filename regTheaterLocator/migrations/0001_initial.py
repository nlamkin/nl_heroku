# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('show_name', models.CharField(max_length=30)),
                ('creation_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='entry_creators')),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('zip_code', models.CharField(blank=True, max_length=10)),
                ('style', models.CharField(blank=True, max_length=10)),
                ('admin', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, related_name='theater_admin')),
            ],
        ),
        migrations.AddField(
            model_name='production',
            name='theater',
            field=models.ForeignKey(to='regTheaterLocator.Theater'),
        ),
        migrations.AddField(
            model_name='production',
            name='updated_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='entry_updator'),
        ),
    ]
