# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-21 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20170119_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
