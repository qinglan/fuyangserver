# Generated by Django 2.1.2 on 2019-01-28 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PictureText', '0004_picturetextpaper_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturetextpaper',
            name='buy_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='购买截止日期'),
        ),
        migrations.AddField(
            model_name='picturetextpaper',
            name='sequeue',
            field=models.IntegerField(default=9999, verbose_name='排序'),
        ),
    ]
