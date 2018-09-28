from abc import abstractmethod

from django.db import models

# Create your models here.

from users.models import User
from study.models import VideoCurriculum, VideoInfoLecture, VideoInfoStudyFuyang
import django.utils.timezone as timezone


class OrderBase(models.Model):
    register_date = models.DateTimeField('购买时间', default=timezone.now, editable=False)
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='购买者')
    apply_bill = models.BooleanField('是否已经申请了发票', default=False)
    is_draw_bill = models.BooleanField('是否已经开了发票', default=False)
    taitou_type = models.IntegerField('发票类型,1:个人，2：公司', default=1)  # type:
    taitou_text = models.CharField('抬头', max_length=256, default='', null=True, blank=True)
    recognition_id = models.CharField('纳税人识别号', max_length=256, default='', null=True, blank=True)
    email = models.EmailField('收件电子邮箱', max_length=256, default='', null=True, blank=True)
    price = models.IntegerField('价格', default=0)
    invoice_date = models.DateTimeField('申请发票时间', auto_now=True, editable=False)

    def get_order_id(self):
        return self.register_date.strftime('%Y%m%d%H%M%S') + str(self.pk).zfill(6)

    def __str__(self):
        return self.get_order_id()

    @abstractmethod
    def get_name(self):
        return "OrderBase名字"

    @abstractmethod
    def get_goods_url(self):
        return "/"

    class Meta:
        verbose_name = 'o订单'
        verbose_name_plural = 'o订单'
        ordering = ['-register_date']


class VideoCurriculumOrder(OrderBase):
    video_curriculum = models.ForeignKey(VideoCurriculum, on_delete=models.CASCADE, blank=True, verbose_name='所属视频课程')

    def __str__(self):
        return self.get_order_id()

    @abstractmethod
    def get_name(self):
        return self.video_curriculum.name

    @abstractmethod
    def get_goods_url(self):
        return self.video_curriculum.get_absolute_url()

    class Meta:
        verbose_name = 'o1课程订单'
        verbose_name_plural = 'o1课程订单'
        ordering = ['-register_date']


class VideoInfoLectureOrder(OrderBase):
    video = models.ForeignKey(VideoInfoLecture, on_delete=models.CASCADE, blank=True,
                              verbose_name='所属免费视频讲座视频')

    def __str__(self):
        return self.get_order_id()

    @abstractmethod
    def get_name(self):
        return self.video.name

    @abstractmethod
    def get_goods_url(self):
        return self.video.get_absolute_url()

    class Meta:
        verbose_name = 'o1免费视频讲座视频订单'
        verbose_name_plural = 'o1免费视频讲座视频订单'
        ordering = ['-register_date']


class VideoInfoStudyFuyangOrder(OrderBase):
    video = models.ForeignKey(VideoInfoStudyFuyang, on_delete=models.CASCADE, blank=True,
                              verbose_name='所属天天乐视频')

    def __str__(self):
        return self.get_order_id()

    @abstractmethod
    def get_name(self):
        return self.video.name

    @abstractmethod
    def get_goods_url(self):
        return self.video.get_absolute_url()

    class Meta:
        verbose_name = 'o1天天乐视频订单'
        verbose_name_plural = 'o1天天乐视频订单'
        ordering = ['-register_date']


class Collection(models.Model):
    class_name = models.CharField('类名', max_length=256, default='', null=True, blank=True)
    item_pk = models.IntegerField('收藏的pk', default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='收藏者',default=None)

    def __str__(self):
        return str(self.get_item())

    def get_absolute_url(self):
        return self.get_item().get_absolute_url()

    def get_image_url(self):
        i = self.get_item().image
        return self.get_item().image.url

    def get_item(self):
        if self.class_name == 'VideoCurriculum':
            vs = VideoCurriculum.objects.filter(pk=self.item_pk)
            if len(vs) > 0:
                return vs[0]
        elif self.class_name == 'VideoInfoLecture':
            vs = VideoInfoLecture.objects.filter(pk=self.item_pk)
            if len(vs) > 0:
                return vs[0]
        elif self.class_name == 'VideoInfoStudyFuyang':
            vs = VideoInfoStudyFuyang.objects.filter(pk=self.item_pk)
            if len(vs) > 0:
                return vs[0]

        return None

    @staticmethod
    def is_collection(user, instance):
        class_name = instance.class_name()
        item_pk = instance.pk
        return len(Collection.objects.filter(class_name=class_name, item_pk=item_pk, author=user)) > 0

    @staticmethod
    def save_collection(user, instance):
        class_name = instance.class_name()
        item_pk = instance.pk
        if Collection.is_collection(user, instance):
            return
        c = Collection.objects.create(class_name=class_name, item_pk=item_pk, author=user)
        c.save()

    @staticmethod
    def cancel_collection(user, instance):
        class_name = instance.class_name()
        item_pk = instance.pk
        Collection.objects.filter(class_name=class_name, item_pk=item_pk, author=user).delete()

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = '收藏'
        ordering = ['-pk']
