# Generated by Django 2.1.2 on 2019-04-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0022_auto_20190413_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoinfolectureclassfy',
            name='show_face',
            field=models.CharField(choices=[('0', '一行两列'), ('1', '一行三列')], default='0', max_length=2, verbose_name='显示方式'),
        ),
    ]