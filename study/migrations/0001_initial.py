# Generated by Django 2.0.7 on 2018-08-28 13:16

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingBanners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='广告名')),
                ('image', models.ImageField(upload_to='image', verbose_name='封面 1921×601 px')),
                ('url', models.CharField(db_index=True, max_length=256, verbose_name='图文栏目网址')),
            ],
            options={
                'verbose_name_plural': 'z2课程报名页面图片维护',
                'verbose_name': 'z2课程报名页面图片维护',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CurriculumOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='订单名')),
            ],
            options={
                'verbose_name_plural': '课程评论',
                'verbose_name': '课程评论',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CurriculumTaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='任务名')),
                ('tips', models.CharField(default='', max_length=256, verbose_name='提示')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='任务创建时间')),
            ],
            options={
                'verbose_name_plural': '任务',
                'verbose_name': '任务',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CurriculumTaskInfoJobAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='', verbose_name='作业评语')),
                ('job_content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='作业回答')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='答题时间')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='答题者')),
            ],
            options={
                'verbose_name_plural': 'a5直播课程作业答案',
                'verbose_name': 'a5直播课程作业答案',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='GraphicArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='图文标题')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='图文网址')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
                ('image', models.ImageField(upload_to='image', verbose_name='封面')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('published', models.BooleanField(default=True, verbose_name='正式发布')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '图文类页面管理',
                'verbose_name': '图文类页面管理',
            },
        ),
        migrations.CreateModel(
            name='GraphicColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='图文栏目名称')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='图文栏目网址')),
                ('intro', models.TextField(default='', verbose_name='图文栏目简介')),
            ],
            options={
                'verbose_name_plural': '图文栏目',
                'verbose_name': '图文栏目',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GraphicComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='图文评论')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('score', models.IntegerField(verbose_name='评论得分')),
                ('ascription', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='study.GraphicArticle', verbose_name='所属图文')),
            ],
            options={
                'verbose_name_plural': '图文评论',
                'verbose_name': '图文评论',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MianInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image', verbose_name='主页图标 500x100 px')),
                ('text_1', models.CharField(max_length=256, verbose_name='黑色文字')),
                ('text_2', models.CharField(max_length=256, verbose_name='灰色文字')),
            ],
            options={
                'verbose_name_plural': 'z1主页信息维护',
                'verbose_name': 'z1主页信息维护',
            },
        ),
        migrations.CreateModel(
            name='TaskInfoVideoAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=256, verbose_name='直播问答')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='提问时间')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': 'a直播问答',
                'verbose_name': 'a直播问答',
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='TaskInfoVideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=256, verbose_name='直播评论')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': 'a直播评论',
                'verbose_name': 'a直播评论',
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='TaskLiveFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='资料名字')),
                ('file', models.FileField(upload_to='files/', verbose_name='资料文件')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='上传时间')),
            ],
            options={
                'verbose_name_plural': 'a4直播课程资料',
                'verbose_name': 'a4直播课程资料',
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='VideoClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='标题')),
                ('index', models.IntegerField(default=0, verbose_name='序号')),
            ],
            options={
                'verbose_name_plural': 'a2直播课程章节',
                'verbose_name': 'a2直播课程章节',
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='VideoColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='视频栏目名称')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='英文名')),
                ('intro', models.TextField(default='', verbose_name='视频栏目简介')),
                ('image', models.ImageField(upload_to='image', verbose_name='封面')),
                ('subcourse', models.IntegerField(verbose_name='子课程数')),
            ],
            options={
                'verbose_name_plural': '视频栏目',
                'verbose_name': '视频栏目',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VideoCurriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='视频课程名称')),
                ('intro', models.CharField(max_length=256, verbose_name='简介')),
                ('introduce', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='视频课程介绍')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='有效期开始时间')),
                ('stop_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='有效期结束时间')),
                ('buy_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='购买截止日期')),
                ('plan', models.CharField(default='', max_length=256, verbose_name='教学计划')),
                ('image', models.ImageField(upload_to='image', verbose_name='封面 480x270 px')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('users', models.ManyToManyField(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='已购人员')),
            ],
            options={
                'verbose_name_plural': 'a1直播课程',
                'verbose_name': 'a1直播课程',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VideoCurriculumComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=256, verbose_name='课程评论')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='注册时间')),
                ('score', models.IntegerField(verbose_name='评论得分')),
                ('ascription', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='study.VideoCurriculum', verbose_name='所属课程')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': 'a6直播课程评论',
                'verbose_name': 'a6直播课程评论',
                'ordering': ['register_date'],
            },
        ),
        migrations.CreateModel(
            name='VideoCurriculumFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='资料名字')),
                ('file', models.FileField(upload_to='files/', verbose_name='资料文件')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='提问时间')),
                ('ascription', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='study.VideoCurriculum', verbose_name='所属课程')),
            ],
            options={
                'verbose_name_plural': 'a4直播课程资料',
                'verbose_name': 'a4直播课程资料',
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256, verbose_name='视频名字')),
                ('introduce', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='视频介绍')),
                ('url', models.CharField(default='', max_length=256, verbose_name='视频地址')),
                ('image', models.ImageField(null=True, upload_to='image', verbose_name='封面')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='开始时间')),
                ('views_count', models.IntegerField(default=0, editable=False, verbose_name='浏览次数')),
            ],
            options={
                'verbose_name_plural': '点播视频',
                'verbose_name': '点播视频',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CurriculumTaskInfoJob',
            fields=[
                ('curriculumtaskinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='study.CurriculumTaskInfo')),
                ('job_questions', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='作业题目')),
                ('job_answer', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='作业答案')),
            ],
            options={
                'verbose_name_plural': 'a5直播课程作业',
                'verbose_name': 'a5直播课程作业',
                'ordering': ['name'],
            },
            bases=('study.curriculumtaskinfo',),
        ),
        migrations.CreateModel(
            name='CurriculumTaskInfoVideo',
            fields=[
                ('curriculumtaskinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='study.CurriculumTaskInfo')),
                ('introduce', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='直播介绍')),
                ('live_id', models.CharField(blank=True, default='30010', max_length=256, null=True, verbose_name='直播ID')),
                ('live_key', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='直播KEY')),
                ('live_start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='直播开始时间')),
                ('play_id', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='录播视频ID')),
                ('play_app_id', models.CharField(blank=True, default='1257252657', max_length=256, null=True, verbose_name='录播视频appID')),
                ('expiry_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='回放过期时间')),
            ],
            options={
                'verbose_name_plural': 'a3直播计划',
                'verbose_name': 'a3直播计划',
                'ordering': ['name'],
            },
            bases=('study.curriculumtaskinfo',),
        ),
        migrations.CreateModel(
            name='VideoInfoLecture',
            fields=[
                ('videoinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='study.VideoInfo')),
                ('intro', models.CharField(max_length=256, verbose_name='简介')),
            ],
            options={
                'verbose_name_plural': 'b2免费视频讲座',
                'verbose_name': 'b2免费视频讲座',
                'ordering': ['name'],
            },
            bases=('study.videoinfo',),
        ),
        migrations.CreateModel(
            name='VideoInfoStudyFuyang',
            fields=[
                ('videoinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='study.VideoInfo')),
                ('intro', models.CharField(max_length=256, verbose_name='简介')),
            ],
            options={
                'verbose_name_plural': 'b1天天乐',
                'verbose_name': 'b1天天乐',
                'ordering': ['name'],
            },
            bases=('study.videoinfo',),
        ),
        migrations.AddField(
            model_name='videoclass',
            name='video_curriculum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='study.VideoCurriculum', verbose_name='归属课程'),
        ),
        migrations.AddField(
            model_name='graphicarticle',
            name='graphic_column',
            field=models.ManyToManyField(to='study.GraphicColumn', verbose_name='图文'),
        ),
        migrations.AddField(
            model_name='curriculumtaskinfo',
            name='video_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='study.VideoClass', verbose_name='归属课节'),
        ),
        migrations.AddField(
            model_name='tasklivefile',
            name='ascription',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='study.CurriculumTaskInfoVideo', verbose_name='所属直播任务'),
        ),
        migrations.AddField(
            model_name='taskinfovideocomment',
            name='ascription',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='study.CurriculumTaskInfoVideo', verbose_name='所属直播'),
        ),
        migrations.AddField(
            model_name='taskinfovideoask',
            name='ascription',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='study.CurriculumTaskInfoVideo', verbose_name='所属直播'),
        ),
        migrations.AddField(
            model_name='curriculumtaskinfojobanswer',
            name='job_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='study.CurriculumTaskInfoJob', verbose_name='答案所属题目'),
        ),
    ]
