# Generated by Django 2.1.2 on 2019-04-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0021_auto_20190408_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoinfolectureclassfy',
            name='show_type',
        ),
        migrations.AddField(
            model_name='videovipprice',
            name='min_exchange_ticket_price',
            field=models.IntegerField(default=9999, verbose_name='赠送兑换券最小价格'),
        ),
    ]
