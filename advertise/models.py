from django.db import models


# Create your models here.
class AdvertisingBanners(models.Model):
    '课程报名页面顶部广告'
    name = models.CharField('广告名', max_length=256)
    image = models.ImageField('封面 1921×601 px', upload_to='image')
    url = models.CharField('图文栏目网址', max_length=256, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'z2课程报名页面图片维护'
        verbose_name_plural = 'z2课程报名页面图片维护'
        ordering = ['name']


class VideoInfoLectureBanners(models.Model):
    '图文栏目、视频区、资料区页面广告'
    name = models.CharField('广告名', max_length=256)
    image = models.ImageField('封面 1921×601 px', upload_to='image')
    url = models.CharField('图文栏目网址', max_length=256, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图文页面广告维护'
        verbose_name_plural = '图文页面广告维护'
        ordering = ['name']


class VideoInfoStudyFuyangBanners(models.Model):
    '直播区页面广告'
    name = models.CharField('广告名', max_length=256)
    image = models.ImageField('封面 1921×601 px', upload_to='image')
    url = models.CharField('图文栏目网址', max_length=256, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '直播区页面广告维护'
        verbose_name_plural = '直播区页面广告维护'
        ordering = ['name']

class VideoAlternateBanners(models.Model):
    '视频区首页顶部轮播图片'
    name = models.CharField('广告名', max_length=256)
    image = models.ImageField('封面 2:1 (建议:360px * 180 px ) ', upload_to='image')
    url = models.CharField('图文栏目网址', max_length=256, db_index=True)
    sequence = models.IntegerField('排序', default=9999)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频区滚动页面广告维护'
        verbose_name_plural = '视频区滚动页面广告维护'
        ordering = ['sequence']


class VideoInnerAdBanners(models.Model):
    '视频首页内部广告图片'
    name = models.CharField('广告名', max_length=256)
    location = models.CharField('广告位置（填写视频一级分类名称）', max_length=256)
    image = models.ImageField('封面 2:1 (建议:360px * 180 px )', upload_to='image')
    url = models.CharField('图文栏目网址', max_length=256, db_index=True)
    sequence = models.IntegerField('排序', default=9999)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频首页内部广告图片维护'
        verbose_name_plural = '视频首页内部广告图片维护'
        ordering = ['sequence']
