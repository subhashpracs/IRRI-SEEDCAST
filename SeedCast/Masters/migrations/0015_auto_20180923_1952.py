# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0014_auto_20180923_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer_registration',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 23, 19, 52, 53, 432822)),
        ),
    ]