# Generated by Django 2.0.7 on 2018-08-21 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180808_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
    ]