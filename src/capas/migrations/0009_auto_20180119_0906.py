# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capas', '0008_auto_20180119_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comunidad',
            old_name='terrtitorio',
            new_name='territorio',
        ),
    ]