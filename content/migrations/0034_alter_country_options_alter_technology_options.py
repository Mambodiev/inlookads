# Generated by Django 4.1.6 on 2023-04-05 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0033_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'Technologies'},
        ),
    ]