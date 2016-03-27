# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 10:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 26, 10, 16, 14, 620928, tzinfo=utc), verbose_name='Was created'),
            preserve_default=False,
        ),
    ]
