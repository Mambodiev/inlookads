# Generated by Django 4.1.6 on 2023-03-09 07:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_course_pricing_tiers'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='call_to_action',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
