# Generated by Django 2.1.2 on 2019-02-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocurriculum',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='是否展示'),
        ),
    ]
