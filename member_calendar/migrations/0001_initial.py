# Generated by Django 2.2.8 on 2019-12-09 21:52

import common.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberCalendarEvent',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('event_date', models.DateField(verbose_name='Event Date')),
                ('event_start_time', models.TimeField(verbose_name='Start time')),
                ('event_end_time', models.TimeField(verbose_name='End time')),
                ('wheelchair_accessible', models.BooleanField(default=False)),
                ('asl_available', models.BooleanField(default=False)),
                ('body', wagtail.core.fields.StreamField([('banner_image', wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock(required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('alt_text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('photo_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')])), ('caption', wagtail.core.blocks.CharBlock(max_length=255)), ('caption_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('tl', 'Left'), ('tr', 'Right'), ('tc', 'Center')]))])), ('h1', common.blocks.HeaderH1(classname='full title')), ('subhead', common.blocks.Subhead(classname='full title')), ('block_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock(classname='full', max_length=255, required=True))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255)), ('cta_copy', wagtail.core.blocks.CharBlock(max_length=255)), ('button_title', wagtail.core.blocks.CharBlock(max_length=255)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_external_link', wagtail.core.blocks.URLBlock(required=False))])), ('small_call_to_action', wagtail.core.blocks.StructBlock([('button_copy', wagtail.core.blocks.CharBlock(max_length=32)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_external_link', wagtail.core.blocks.URLBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('tl', 'Left'), ('tr', 'Right'), ('tc', 'Center')]))])), ('embed_code', wagtail.core.blocks.StructBlock([('embed_code', wagtail.core.blocks.TextBlock(required=True))]))])),
                ('location_street_address', models.CharField(blank=True, max_length=255)),
                ('location_city', models.CharField(blank=True, max_length=255)),
                ('location_zip_code', models.CharField(blank=True, max_length=5)),
                ('location_state', models.CharField(blank=True, max_length=100)),
                ('location_name', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MemberCalendarHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
    ]
