# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capas', '0011_auto_20180119_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='vivienda',
            name='numero',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]