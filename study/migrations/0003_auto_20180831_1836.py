# Generated by Django 2.0.7 on 2018-08-31 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_auto_20180830_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videocurriculumfile',
            options={'ordering': ['-register_date'], 'verbose_name': 'a4课程资料', 'verbose_name_plural': 'a4课程资料'},
        ),
    ]