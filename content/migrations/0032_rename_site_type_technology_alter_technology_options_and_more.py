# Generated by Django 4.1.6 on 2023-04-04 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0031_site_type_remove_course_ads_type_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Site_type',
            new_name='Technology',
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name': 'Technologies'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='site_type',
            new_name='technologies',
        ),
    ]
