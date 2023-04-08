# Generated by Django 4.1.6 on 2023-04-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0029_alter_course_primary_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='primary_category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='secondary_categories',
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='content.category'),
        ),
    ]