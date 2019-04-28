# -*- coding: utf-8 -*-
from abc import abstractmethod

from django.db import models

# Create your models here.
import os
import datetime
from django.db import models
from DjangoUeditor.models import UEditorField
from users.models import User
import django.utils.timezone as timezone
from django.urls import reverse
from fuyangserver.settings import MEDIA_URL


class VideoColumn(models.Model):
    name = models.CharField('视频栏目名称', max_length=256)
    slug = models.CharField('英文名', max_length=256, db_index=True)
    intro = models.TextField('视频栏目简介', default='')

    image = models.ImageField('封面', upload_to='image')
    subcourse = models.IntegerField('子课程数')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频栏目'
        verbose_name_plural = '视频栏目'
        ordering = ['name']


class VideoCurriculum(models.Model):
    name = models.CharField('视频课程名称', max_length=256)
    intro = models.CharField('简介', max_length=256)
    introduce = UEditorField('视频课程介绍', height=300, width=1000,
                             default=u'', blank=True, imagePath="uploads/images/",
                             toolbars='besttome', filePath='uploads/files/')

    start_time = models.DateTimeField('有效期开始时间', null=True, editable=True, default=timezone.now)
    stop_time = models.DateTimeField('有效期结束时间', null=True, editable=True, default=timezone.now)
    buy_time = models.DateTimeField('购买截止日期', editable=True, default=timezone.now)

    plan = models.CharField('教学计划', default='', max_length=256)

    image = models.ImageField('封面 480x270 px', upload_to='image')

    price = models.IntegerField('价格')

    count = models.IntegerField('课程数', default=0)
    sequeue = models.IntegerField('排序', default=9999)
    is_show = models.BooleanField('是否展示', default=True)
    views_count = models.IntegerField('浏览次数', default=0, editable=False)

    TYPE_CHOICE = (
        (u'0', u'免费'),
        (u'1', u'余额/微信'),
        (u'2', u'听课券'),
    )
    pay_type = models.CharField('支付方式', max_length=2, choices=TYPE_CHOICE, default='0')

    def __str__(self):
        return self.name

    def class_name(self):
        return 'VideoCurriculum'

    def get_absolute_url(self):
        return reverse('video_curriculum_detail', args=(self.pk,))

    def get_tasks_url(self):
        return reverse('video_curriculum_tasks', args=(self.pk,))

    def get_reviews_url(self):
        return reverse('video_curriculum_reviews', args=(self.pk,))

    def get_material_url(self):
        return reverse('video_curriculum_material', args=(self.pk,))

    def get_material_count(self):
        return len(TaskLiveFile.objects.filter(ascription__video_curriculum=self))

    # 是否正在直播
    def get_live_info(self):
        civs = CurriculumTaskInfoVideo.objects.filter( \
            video_class__video_curriculum=self).order_by('-live_start_time')
        live_info = {'live_url': '', 'last_live_time': ''}
        for civ in civs:
            if civ.is_liveing():
                live_info['live_url'] = civ.get_introduce_url()
                return live_info
            else:
                last_live_time = civ.get_live_last()
                if last_live_time != '' and last_live_time is not None:
                    live_info['last_live_time'] = last_live_time

        return live_info

    def get_material_image(self):
        cs = VideoClass.objects.filter(video_curriculum=self).order_by('-pub_date')
        ret = self.image
        for item in cs:
            civs = CurriculumTaskInfoVideo.objects.filter(
                video_class=item).order_by('-live_start_time')
            if len(civs) == 0:
                ret = item.image
            for civ in civs:
                if civ.is_liveing():
                    return item.image
                elif not civ.is_replay():
                    ret = item.image

        return ret

    def get_comment_count(self):
        '获取评论数'
        return VideoCurriculumComment.objects.filter(ascription=self.pk).count()

    def is_expires(self):
        '是否过期'
        return self.buy_time > datetime.datetime.now()

    class Meta:
        verbose_name = 'a1直播课程'
        verbose_name_plural = 'a1直播课程'
        ordering = ['name']


class GraphicColumn(models.Model):
    '图文栏类别'
    name = models.CharField('图文栏目名称', max_length=256)
    slug = models.CharField('图文栏目网址', max_length=256, db_index=True)
    intro = models.TextField('图文栏目简介', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图文栏目'
        verbose_name_plural = '图文栏目'
        ordering = ['name']


class GraphicArticle(models.Model):
    name = models.CharField('图文标题', max_length=256)

    graphic_column = models.ManyToManyField(GraphicColumn, verbose_name='图文')

    slug = models.CharField('图文网址', max_length=256, db_index=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    image = models.ImageField('封面', upload_to='image')
    register_date = models.DateTimeField('注册时间', auto_now_add=True, editable=True)
    update_date = models.DateTimeField('修改时间', auto_now_add=True, editable=True)

    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图文类页面管理'
        verbose_name_plural = '图文类页面管理'


class CurriculumOrder(models.Model):
    name = models.CharField('订单名', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = '课程评论'
        ordering = ['name']


class GraphicComment(models.Model):
    name = models.CharField('图文评论', max_length=256)
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    ascription = models.ForeignKey(GraphicArticle, on_delete=models.CASCADE, blank=True, verbose_name='所属图文')
    register_date = models.DateTimeField('注册时间', auto_now_add=True, editable=True)
    update_date = models.DateTimeField('修改时间', auto_now_add=True, editable=True)
    score = models.IntegerField('评论得分')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图文评论'
        verbose_name_plural = '图文评论'
        ordering = ['name']


class VideoClass(models.Model):
    name = models.CharField('标题', max_length=256)

    video_curriculum = models.ForeignKey(VideoCurriculum, on_delete=models.CASCADE, null=True, verbose_name='归属课程')

    image = models.ImageField('封面 480x270 px', upload_to='image', null=True)

    pub_date = models.DateTimeField('创建时间', default=timezone.now, editable=False)

    def __str__(self):
        return self.video_curriculum.name + '-' + self.name

    class Meta:
        verbose_name = 'a2直播课程章节'
        verbose_name_plural = 'a2直播课程章节'
        ordering = ['pub_date']


class CurriculumTaskInfo(models.Model):
    name = models.CharField('任务名', max_length=256)
    video_class = models.ForeignKey(VideoClass, on_delete=models.CASCADE, null=True, verbose_name='归属课节')
    tips = models.CharField('提示', max_length=256, default='')
    pub_date = models.DateTimeField('任务创建时间', default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'
        ordering = ['name']


class CurriculumTaskInfoJob(CurriculumTaskInfo):
    job_questions = UEditorField('作业题目', height=300, width=1000,
                                 default=u'', blank=True, imagePath="uploads/images/",
                                 toolbars='besttome', filePath='uploads/files/')

    job_answer = UEditorField('作业答案', height=300, width=1000,
                              default=u'', blank=True, imagePath="uploads/images/",
                              toolbars='besttome', filePath='uploads/files/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class_job', args=(self.pk,))

    def get_parent_url(self):
        return self.video_class.video_curriculum.get_absolute_url()

    def get_iframe_url(self):
        return reverse('class_job_iframe', args=(self.pk,))

    def get_post_url(self):
        return reverse('class_job_iframe_post', args=(self.pk,))

    class Meta:
        verbose_name = 'a5直播课程作业'
        verbose_name_plural = 'a5直播课程作业'
        ordering = ['name']


class CurriculumTaskInfoJobAnswer(models.Model):
    comment = models.TextField('作业评语', default='')

    job_parent = models.ForeignKey(CurriculumTaskInfoJob, on_delete=models.CASCADE,
                                   blank=True, null=True, verbose_name='答案所属题目')

    job_content = UEditorField('作业回答', height=300, width=1000,
                               default=u'', blank=True, imagePath="uploads/images/",
                               toolbars='besttome', filePath='uploads/files/')

    pub_date = models.DateTimeField('答题时间', default=timezone.now, editable=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='答题者')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'a5直播课程作业答案'
        verbose_name_plural = 'a5直播课程作业答案'
        ordering = ['pub_date']


class CurriculumTaskInfoVideo(CurriculumTaskInfo):
    introduce = UEditorField('直播介绍', height=300, width=1000,
                             default=u'', blank=True, imagePath="uploads/images/",
                             toolbars='besttome', filePath='uploads/files/')

    live_id = models.CharField('直播ID', null=True, blank=True, max_length=256, default='30010')

    live_key = models.CharField('直播KEY', null=True, blank=True, max_length=256, default='')

    live_start_time = models.DateTimeField('直播开始时间', default=timezone.now)

    play_id = models.CharField('录播视频ID', null=True, blank=True, max_length=256, default='')

    play_app_id = models.CharField('录播视频appID', null=True, blank=True, max_length=256, default='1257252657')

    expiry_time = models.DateTimeField('回放过期时间', default=timezone.now)

    live_image = models.CharField('当前直播显示的图片', null=True, blank=True, max_length=256, default='')

    image_show_time = models.TextField('图片显示时间', null=True, blank=True, default='')

    speaking = models.BooleanField('是否可以发言', default=True)

    def get_introduce_url(self):
        return reverse('tasklive_introduce', args=(self.pk,))

    def get_ask_url(self):
        return reverse('tasklive_ask', args=(self.pk,))

    def get_reviews_url(self):
        return reverse('tasklive_reviews', args=(self.pk,))

    def get_iframe_introduce_url(self):
        return reverse('iframe_tasklive_introduce', args=(self.pk,))

    def get_iframe_tasklive_introduce_nextimage_url(self):
        return reverse('iframe_tasklive_introduce_nextimage', args=(self.pk,))

    def get_iframe_ask_url(self):
        return reverse('iframe_tasklive_ask', args=(self.pk,))

    def get_iframe_reviews_url(self):
        return reverse('iframe_tasklive_reviews', args=(self.pk,))

    def get_iframe_material_url(self):
        return reverse('iframe_tasklive_material', args=(self.pk,))

    def get_iframe_reviews_post_url(self):
        return reverse('iframe_tasklive_reviews_post', args=(self.pk,))

    def get_iframe_ask_post_url(self):
        return reverse('iframe_tasklive_ask_post', args=(self.pk,))

    def is_replay(self):
        if self.play_id != '' and self.play_id is not None:
            return True

        return False

    def is_liveing(self):
        if self.live_key != '' and self.live_key is not None:
            if self.play_id == '' or self.play_id is None:
                return True
        return False

    def get_live_last(self):
        if self.live_start_time > datetime.datetime.now() and \
                (self.live_key == '' or self.live_key is None):
            dt = (self.live_start_time - datetime.datetime.now())
            return '' + str(dt.days) + "天" + \
                   str(int(dt.seconds / 3600)) + "小时" + \
                   str(int(dt.seconds / 60) % 60) + "分钟"
        return ''

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'a3直播计划'
        verbose_name_plural = 'a3直播计划'
        ordering = ['name']


class VideoCurriculumComment(models.Model):
    '直播课程评论'
    message = models.CharField('课程评论', max_length=256)
    ascription = models.ForeignKey(VideoCurriculum, on_delete=models.CASCADE, blank=True, verbose_name='所属课程')
    register_date = models.DateTimeField('注册时间', default=timezone.now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='作者')
    score = models.IntegerField('评论得分')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'a6直播课程评论'
        verbose_name_plural = 'a6直播课程评论'
        ordering = ['register_date']


class VideoInfo(models.Model):
    '视频区基类'
    name = models.CharField('视频名字', default='', max_length=256)

    introduce = UEditorField('视频介绍', height=300, width=1000,
                             default=u'', blank=True, imagePath="uploads/images/",
                             toolbars='besttome', filePath='uploads/files/')

    play_id = models.CharField('录播视频文件ID', null=True, blank=True, max_length=256, default='')

    play_app_id = models.CharField('录播视频appID', null=True, blank=True, max_length=256, default='1257252657')

    image = models.ImageField('封面', upload_to='image', null=True, help_text='一行两列 304 x 171  一行三列 240x324')
    pub_date = models.DateTimeField('开始时间', default=timezone.now, editable=False)

    views_count = models.IntegerField('浏览次数', default=0, editable=False)

    price = models.IntegerField('价格', default=0)

    def __str__(self):
        return self.name

    @abstractmethod
    def get_collection_url(self):
        return '/'

    @abstractmethod
    def get_absolute_url(self):
        return reverse('video_curriculum_reviews', args=(self.pk,))

    @abstractmethod
    def get_comment_count(self):
        return 0

    @abstractmethod
    def get_post_url(self):
        return "/"

    @abstractmethod
    def get_buy_url(self):
        return "/"

    class Meta:
        verbose_name = '点播视频'
        verbose_name_plural = verbose_name
        ordering = ['name']


class VideoInfoLectureClassfy(models.Model):
    '视频区一级分类表'
    message = models.CharField('视频分类', max_length=256)
    remark = models.TextField('分类相关说明', max_length=256)
    register_date = models.DateTimeField('添加时间', default=timezone.now, editable=False)
    show_face = models.IntegerField('显示方式', choices=((0, u'一行两列'), (1, u'一行三列'),), default=0)
    bgcolor = models.CharField('背景颜色', max_length=50, default='#F0EDFB', help_text='十六进制颜色值')
    thumbnail = models.FileField('栏目图标', upload_to='image/', help_text='图片大小：36x36')
    sequeue = models.IntegerField('排序', default=9999)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = '视频区一级分类表'
        verbose_name_plural = verbose_name
        ordering = ['register_date']


class VideoVipPrice(models.Model):
    '视频区VIP会员价格表'
    VIP_price = models.IntegerField('VIP价格', default=9999)
    min_exchange_ticket_price = models.IntegerField('赠送兑换券最小价格', default=9999)

    def __str__(self):
        return str(self.VIP_price)

    class Meta:
        verbose_name = '视频区VIP会员价格表'
        verbose_name_plural = verbose_name
        ordering = ['VIP_price']


# 支付方式
PAYTYPE = (
    ('0', u'免费'),
    ('1', u'余额/微信'),
    ('2', u'听课券'),
    ('3', u'VIP'),
)


class VideoInfoLecture(VideoInfo):
    '视频区'
    intro = models.CharField('简介', max_length=256)
    sequeue = models.IntegerField('排序', default=9999)

    pay_type = models.CharField('支付方式', max_length=2, choices=PAYTYPE, default='0')

    lecture_type_first = models.ForeignKey(VideoInfoLectureClassfy, related_name='vlist', on_delete=models.CASCADE,
                                           blank=True, null=True,
                                           verbose_name='视频一级分类')

    lecture_type_second = models.CharField('视频二级分类', max_length=2, choices=(('0', u'最新'), ('1', u'全部')), default='0')

    def __str__(self):
        return self.name

    def class_name(self):
        return 'VideoInfoLecture'

    def hasItems(self):
        '判断是否有剧集'
        return self.details.count() > 1

    @abstractmethod
    def get_collection_url(self):
        return reverse('videoplaylecture_collection', args=(self.pk,))

    @abstractmethod
    def get_absolute_url(self):
        return reverse('videoplaylecture', args=(self.pk,))

    def get_comment_count(self):
        return len(VideoInfoLectureComment.objects.filter(ascription=self))

    @abstractmethod
    def get_post_url(self):
        return reverse('videoplaylecture_comment', args=(self.pk,))

    @abstractmethod
    def get_buy_url(self):
        return reverse('buyvideolecture', args=(self.pk,))

    class Meta:
        verbose_name = '视频区'
        verbose_name_plural = verbose_name
        ordering = ['sequeue']


class VideoInfoLectureDetails(models.Model):
    '视频区剧集子表'
    play_id = models.CharField('录播视频文件ID', max_length=256)
    play_app_id = models.CharField('录播视频appID', max_length=256, default='1257252657')
    # pay_type = models.CharField('支付方式', max_length=2, choices=PAYTYPE, default='0')    暂时不设置单集价格
    sequence = models.IntegerField('第几集', default=1)
    updatetime = models.DateTimeField('更新日期', auto_now=True)
    belongto = models.ForeignKey(VideoInfoLecture, verbose_name='所属视频大类', related_name='details',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.belongto.name + '-' + str(self.id)

    class Meta:
        verbose_name = '视频区剧集'
        verbose_name_plural = verbose_name
        ordering = ['sequence']


class VideoInfoLectureComment(models.Model):
    '视频区评论'
    message = models.CharField('视频评论', max_length=256)
    ascription = models.ForeignKey(VideoInfoLecture, on_delete=models.CASCADE, blank=True, verbose_name='所属视频')
    register_date = models.DateTimeField('注册时间', default=timezone.now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='作者')
    score = models.IntegerField('评论得分', default=0)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = '视频区评论'
        verbose_name_plural = '视频区评论'
        ordering = ['-register_date']


class VideoInfoStudyFuyang(VideoInfo):
    intro = models.CharField('简介', max_length=256)
    sequeue = models.IntegerField('排序', default=9999)

    def __str__(self):
        return self.name

    @abstractmethod
    def get_collection_url(self):
        return reverse('videoplaystudyfuyang_collection', args=(self.pk,))

    def class_name(self):
        return 'VideoInfoStudyFuyang'

    @abstractmethod
    def get_absolute_url(self):
        return reverse('videoplaystudyfuyang', args=(self.pk,))

    @abstractmethod
    def get_comment_count(self):
        return len(VideoInfoStudyFuyangComment.objects.filter(ascription=self))

    @abstractmethod
    def get_post_url(self):
        return reverse('videoplaystudyfuyang_comment', args=(self.pk,))

    @abstractmethod
    def get_buy_url(self):
        return reverse('buystudyfuyang', args=(self.pk,))

    class Meta:
        verbose_name = 'b1天天乐'
        verbose_name_plural = 'b1天天乐'
        ordering = ['name']


class VideoInfoStudyFuyangComment(models.Model):
    message = models.CharField('视频评论', max_length=256)
    ascription = models.ForeignKey(VideoInfoStudyFuyang, on_delete=models.CASCADE, blank=True, verbose_name='所属视频')
    register_date = models.DateTimeField('注册时间', default=timezone.now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='作者')
    score = models.IntegerField('评论得分', default=0)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'bz免费视频讲座视频评论'
        verbose_name_plural = 'bz免费视频讲座视频评论'
        ordering = ['-register_date']


class TaskInfoVideoComment(models.Model):
    message = models.CharField('直播评论', max_length=256)
    ascription = models.ForeignKey(CurriculumTaskInfoVideo, on_delete=models.CASCADE, blank=True, verbose_name='所属直播')
    register_date = models.DateTimeField('评论时间', auto_now_add=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='作者')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'a7直播评论'
        verbose_name_plural = 'a7直播评论'
        ordering = ['-register_date']


class TaskInfoVideoAsk(models.Model):
    message = models.CharField('直播问答', max_length=256)
    ascription = models.ForeignKey(CurriculumTaskInfoVideo, on_delete=models.CASCADE, blank=True,
                                   verbose_name='所属直播')
    register_date = models.DateTimeField('提问时间', auto_now_add=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='作者')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'a直播问答'
        verbose_name_plural = 'a直播问答'
        ordering = ['-register_date']


class VideoCurriculumFile(models.Model):
    name = models.CharField('资料名字', max_length=256)
    file = models.FileField('资料文件', upload_to='files/')
    ascription = models.ForeignKey(VideoCurriculum, on_delete=models.CASCADE, blank=True,
                                   verbose_name='所属课程')
    register_date = models.DateTimeField('提问时间', default=timezone.now, editable=False)

    def get_download_url(self):
        path = os.path.join(MEDIA_URL, self.file.url)
        return path

    def get_file_size(self):
        fsize = self.file.size / float(1024 * 1024)
        return round(fsize, 2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'a4课程资料'
        verbose_name_plural = 'a4课程资料'
        ordering = ['-register_date']


class MianInfo(models.Model):
    '站点信息配置'
    name = models.CharField('站点名称', max_length=256, default='扶阳医学')
    text_1 = models.CharField('站点关键字', max_length=256)
    text_2 = models.CharField('站点描述', max_length=256)
    image = models.ImageField('主页图标 500x100 px', upload_to='image')
    background = models.ImageField('背景图片', upload_to='image', default='image/title_bg.png')
    wordsclean = models.TextField('评论内容过虑', max_length=256, blank=True, help_text='使用,|;分隔')

    def __str__(self):
        return self.text_1

    class Meta:
        verbose_name = '站点信息配置'
        verbose_name_plural = verbose_name


class TaskLiveFile(models.Model):
    name = models.CharField('资料名字', max_length=256)
    file = models.FileField('资料文件', upload_to='files/')
    ascription = models.ForeignKey(VideoClass, on_delete=models.CASCADE, blank=True,
                                   verbose_name='所属章节')
    register_date = models.DateTimeField('上传时间', default=timezone.now, editable=False)

    def get_download_url(self):
        path = os.path.join(MEDIA_URL, self.file.url)
        return path

    def get_file_size(self):
        fsize = self.file.size / float(1024 * 1024)
        return round(fsize, 2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'a4直播章节资料'
        verbose_name_plural = 'a4直播章节资料'
        ordering = ['-register_date']


class SinglePage(models.Model):
    '单页面实体'
    name = models.CharField('标题', max_length=256)
    content = UEditorField('正文', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')
    updatetime = models.DateTimeField('更新日期', default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '单页面维护'
        verbose_name_plural = '单页面维护'
        db_table = 'singlepage'
        ordering = ['id']


class DataLst(models.Model):
    '资料区'
    name = models.CharField('标题', max_length=256)
    introduce = models.TextField('简介', default='')
    content = UEditorField('正文', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')
    image = models.ImageField('封面', upload_to='image')
    file = models.FileField('文件', upload_to='files/')
    updatetime = models.DateTimeField('更新日期', default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资料区'
        verbose_name_plural = '资料区'
        db_table = 'datalist'
        ordering = ['id']
