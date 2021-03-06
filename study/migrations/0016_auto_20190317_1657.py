# Generated by Django 2.1.2 on 2019-03-17 16:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0015_videocurriculum_is_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoInfoLectureClassfy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=256, verbose_name='视频分类')),
                ('remark', models.TextField(max_length=256, verbose_name='分类相关说明')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '视频区一级分类表',
                'verbose_name_plural': '视频区一级分类表',
                'ordering': ['-register_date'],
            },
        ),
        migrations.AddField(
            model_name='videocurriculum',
            name='pay_type',
            field=models.CharField(choices=[('0', '免费'), ('1', '余额/微信'), ('2', '听课券')], default='0', max_length=2, verbose_name='支付方式'),
        ),
        migrations.AddField(
            model_name='videoinfolecture',
            name='lecture_type_second',
            field=models.CharField(choices=[('0', '推荐课程'), ('1', '直播课程'), ('2', '名师课程')], default='0', max_length=2, verbose_name='视频二级分类'),
        ),
        migrations.AddField(
            model_name='videoinfolecture',
            name='pay_type',
            field=models.CharField(choices=[('0', '免费'), ('1', '余额/微信'), ('2', '听课券')], default='0', max_length=2, verbose_name='支付方式'),
        ),
        migrations.AddField(
            model_name='videoinfolecture',
            name='lecture_type_first',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='study.VideoInfoLectureClassfy', verbose_name='视频一级分类'),
        ),
    ]
