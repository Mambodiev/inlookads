# Generated by Django 4.1.6 on 2023-03-29 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_rename_name_course_name_of_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='image_store',
            new_name='store_logo',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='thumbnail',
            new_name='store_thumbnail',
        ),
    ]