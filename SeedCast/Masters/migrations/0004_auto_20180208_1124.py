# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-08 11:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0003_auto_20171228_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer_registration',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 11, 24, 32, 239133)),
        ),
        migrations.AlterField(
            model_name='vawdemand',
            name='date_collected',
            field=models.DateField(default=datetime.datetime(2018, 2, 8, 11, 24, 32, 244105)),
        ),
    ]
