# -*- coding: utf-8 -*-
# Generated by Django 1.9.5.dev20160312175816 on 2016-04-03 10:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_medicines_refill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='expiry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='medicines',
            name='refill',
            field=models.BooleanField(default=False),
        ),
    ]