# Generated by Django 4.1.6 on 2023-04-05 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0034_alter_country_options_alter_technology_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='countries',
        ),
        migrations.AddField(
            model_name='course',
            name='countries',
            field=models.ManyToManyField(max_length=100, to='content.country'),
        ),
    ]
