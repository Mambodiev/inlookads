# Generated by Django 4.1.6 on 2023-03-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='is_instagram',
            new_name='is_pinterest',
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]