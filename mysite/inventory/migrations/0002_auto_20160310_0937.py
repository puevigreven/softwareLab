# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventory',
            new_name='Medicine',
        ),
    ]
