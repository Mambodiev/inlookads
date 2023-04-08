# Generated by Django 4.1.6 on 2023-04-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0030_remove_course_primary_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='ads_type',
        ),
        migrations.RemoveField(
            model_name='course',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='course',
            name='media_type',
        ),
        migrations.RemoveField(
            model_name='course',
            name='technology',
        ),
        migrations.AlterField(
            model_name='course',
            name='button',
            field=models.CharField(default='Buy Now', max_length=250),
        ),
        migrations.AlterField(
            model_name='course',
            name='countries',
            field=models.CharField(default='United States', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.CharField(default='English', max_length=250),
        ),
        migrations.AddField(
            model_name='course',
            name='site_type',
            field=models.ManyToManyField(to='content.site_type'),
        ),
    ]