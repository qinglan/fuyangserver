# Generated by Django 2.0.7 on 2018-10-03 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoinfolecturebanners',
            options={'ordering': ['name'], 'verbose_name': '图文页面广告维护', 'verbose_name_plural': '图文页面广告维护'},
        ),
        migrations.AlterModelOptions(
            name='videoinfostudyfuyangbanners',
            options={'ordering': ['name'], 'verbose_name': '直播区页面广告维护', 'verbose_name_plural': '直播区页面广告维护'},
        ),
    ]
