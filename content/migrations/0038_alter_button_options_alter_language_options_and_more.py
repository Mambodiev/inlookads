# Generated by Django 4.1.6 on 2023-04-05 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0037_rename_language_course_languages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='button',
            options={'verbose_name_plural': 'Buttons'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name_plural': 'Languages'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='button',
            new_name='buttons',
        ),
    ]