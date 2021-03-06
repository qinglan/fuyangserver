# Generated by Django 2.0.7 on 2018-08-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='中国', max_length=256, verbose_name='国'),
        ),
        migrations.AddField(
            model_name='user',
            name='headimgurl',
            field=models.CharField(default='http://thirdwx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/46', max_length=1024, verbose_name='头像URL'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=256, verbose_name='昵称'),
        ),
        migrations.AddField(
            model_name='user',
            name='openid',
            field=models.CharField(default='', max_length=256, verbose_name='微信ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='province',
            field=models.CharField(default='', max_length=256, verbose_name='省'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.IntegerField(default=1, verbose_name='性别'),
        ),
    ]
