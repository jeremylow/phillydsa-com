# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170611_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='og_type',
            field=models.CharField(choices=[('article', 'Article'), ('website', 'Website'), ('book', 'Book'), ('video', 'Video'), ('profile', 'Profile')], default='website', max_length=127),
        ),
    ]