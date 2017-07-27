# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_auto_20170715_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seosettings',
            old_name='organization_name',
            new_name='organization_short_name',
        ),
        migrations.AddField(
            model_name='seosettings',
            name='google_analytics_key',
            field=models.CharField(blank=True, help_text='Google Analytics Key. Should be something like UA-101255774-1.', max_length=255),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='google_site_verification_key',
            field=models.CharField(blank=True, help_text='Verification key for Google Webmaster Tools.', max_length=255),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='keywords',
            field=models.CharField(blank=True, help_text='Comma separated list of keywords describing your website.', max_length=1500),
        ),
        migrations.AddField(
            model_name='seosettings',
            name='organization_full_name',
            field=models.CharField(default='', help_text='The actual name of your local (ie. Philadelphia Local of the Democratic [etc])', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seosettings',
            name='description',
            field=models.CharField(blank=True, help_text='A short description of your local. City, what you are trying to achieve, etc.', max_length=500),
        ),
        migrations.AlterField(
            model_name='seosettings',
            name='logo',
            field=models.ForeignKey(blank=True, help_text='The URL of the logo of your local. Ideally, should be 1200x1200', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]