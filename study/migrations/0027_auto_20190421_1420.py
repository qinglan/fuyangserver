# Generated by Django 2.2 on 2019-04-21 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0026_auto_20190421_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoinfolecturedetails',
            options={'ordering': ['sequence'], 'verbose_name': '视频区剧集', 'verbose_name_plural': '视频区剧集'},
        ),
        migrations.RemoveField(
            model_name='videoinfolecturedetails',
            name='pay_type',
        ),
    ]