# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capas', '0019_auto_20180120_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='censo',
            name='fecha',
            field=models.DateField(),
        ),
    ]