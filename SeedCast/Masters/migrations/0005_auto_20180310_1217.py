# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-10 12:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0004_auto_20180208_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vawdemand',
            old_name='variety2',
            new_name='varietyName',
        ),
        migrations.AlterField(
            model_name='dealer_registration',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 10, 12, 16, 56, 365247)),
        ),
        migrations.AlterField(
            model_name='vawdemand',
            name='date_collected',
            field=models.DateField(default=datetime.datetime(2018, 3, 10, 12, 16, 56, 370261)),
        ),
    ]
