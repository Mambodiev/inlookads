# Generated by Django 4.2 on 2023-04-14 05:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_faq_options_alter_privacy_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='about us', null=True)),
                ('name', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='price', null=True)),
                ('name', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Price',
            },
        ),
        migrations.AlterModelOptions(
            name='privacy',
            options={'verbose_name_plural': 'Privacy'},
        ),
    ]