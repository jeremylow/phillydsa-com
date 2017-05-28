# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_calendar', '0002_auto_20170527_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membercalendarevent',
            name='location_city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='membercalendarevent',
            name='location_state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='membercalendarevent',
            name='location_street_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='membercalendarevent',
            name='location_zip_code',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
