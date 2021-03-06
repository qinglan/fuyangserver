# Generated by Django 2.2 on 2019-04-21 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0023_videoinfolectureclassfy_show_face'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoinfolecture',
            name='viede_set_name',
        ),
        migrations.RemoveField(
            model_name='videoinfolecture',
            name='viede_set_order',
        ),
        migrations.AlterField(
            model_name='videoinfolecture',
            name='lecture_type_second',
            field=models.CharField(choices=[(0, '最新'), (1, '全部')], default='0', max_length=2, verbose_name='视频二级分类'),
        ),
        migrations.AlterField(
            model_name='videoinfolecture',
            name='pay_type',
            field=models.CharField(choices=[(0, '免费'), (1, '余额/微信'), (2, '听课券'), (3, 'VIP')], default='0', max_length=2, verbose_name='支付方式'),
        ),
        migrations.CreateModel(
            name='VideoInfoLectureDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_id', models.CharField(max_length=256, verbose_name='录播视频文件ID')),
                ('play_app_id', models.CharField(default='1257252657', max_length=256, verbose_name='录播视频appID')),
                ('pay_type', models.CharField(choices=[(0, '免费'), (1, '余额/微信'), (2, '听课券'), (3, 'VIP')], default='0', max_length=2, verbose_name='支付方式')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('belongto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='study.VideoInfoLecture', verbose_name='所属视频大类')),
            ],
            options={
                'verbose_name': '视频区剧集',
                'verbose_name_plural': '视频区剧集',
                'ordering': ['id'],
            },
        ),
    ]
