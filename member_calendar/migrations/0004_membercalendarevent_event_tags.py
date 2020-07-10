# Generated by Django 3.0.7 on 2020-06-28 21:17

from django.db import migrations
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('member_calendar', '0003_calendareventtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='membercalendarevent',
            name='event_tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='member_calendar.CalendarEventTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]