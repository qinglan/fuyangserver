# Generated by Django 2.1.2 on 2019-04-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0020_auto_20190407_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoinfolecture',
            name='lecture_type_second',
            field=models.CharField(choices=[('0', '最新'), ('1', '全部')], default='0', max_length=2, verbose_name='视频二级分类'),
        ),
    ]