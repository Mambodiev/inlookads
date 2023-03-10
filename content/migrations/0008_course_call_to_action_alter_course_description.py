# Generated by Django 4.1.6 on 2023-03-09 07:31

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_video_call_to_action_alter_video_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='call_to_action',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
