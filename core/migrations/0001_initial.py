# Generated by Django 4.2 on 2023-05-01 09:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliate_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='Affiliate', null=True)),
                ('name', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField(null=True)),
                ('question', models.CharField(max_length=200, null=True)),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Faq',
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
        migrations.CreateModel(
            name='PrivacyTermsAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'PrivacyTermsAbout',
            },
        ),
    ]
