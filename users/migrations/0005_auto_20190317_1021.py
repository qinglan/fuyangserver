# Generated by Django 2.1.2 on 2019-03-17 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190225_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPaydetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_bill', models.IntegerField(default=0, verbose_name='消费金额')),
                ('pay_type', models.CharField(choices=[('0', '账户余额'), ('1', '听课券'), ('2', '兑换券')], default='0', max_length=2, verbose_name='消费分类')),
                ('pay_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='消费时间')),
                ('remark', models.CharField(blank=True, default='', max_length=256, verbose_name='备注')),
            ],
            options={
                'verbose_name': 'S用户消费记录单',
                'verbose_name_plural': 'S用户消费记录单',
                'ordering': ['-pay_date'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='account_sum',
            field=models.IntegerField(default=0, verbose_name='账户余额'),
        ),
        migrations.AddField(
            model_name='user',
            name='attendance_ticket',
            field=models.IntegerField(default=0, verbose_name='听课券'),
        ),
        migrations.AddField(
            model_name='user',
            name='exchange_ticket',
            field=models.IntegerField(default=0, verbose_name='兑换券'),
        ),
        migrations.AddField(
            model_name='user',
            name='id_checkstate',
            field=models.CharField(choices=[('0', '未审核'), ('1', '审核中'), ('2', '审核通过')], default='0', max_length=2, verbose_name='身份证审核结果'),
        ),
        migrations.AddField(
            model_name='userpaydetails',
            name='purchaser',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='购买者'),
        ),
    ]
