# Generated by Django 4.1.6 on 2023-04-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0035_remove_course_countries_course_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'button',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='button',
        ),
        migrations.RemoveField(
            model_name='course',
            name='language',
        ),
        migrations.AddField(
            model_name='course',
            name='button',
            field=models.ManyToManyField(to='content.button'),
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ManyToManyField(to='content.language'),
        ),
    ]