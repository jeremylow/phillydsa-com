# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_homepage_share_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='og_type',
            field=models.CharField(choices=[('article', 'Article'), ('website', 'Website'), ('book', 'Book'), ('video', 'Video'), ('profile', 'Profile')], default='website', help_text='See Object Types: https://developers.facebook.com/docs/reference/opengraph/', max_length=127, verbose_name='OG Page Type'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='share_image',
            field=models.ForeignKey(blank=True, help_text='Should be larger than 1200 x 630px\n See https://developers.facebook.com/docs/sharing/best-practices#images', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Share Image'),
        ),
    ]