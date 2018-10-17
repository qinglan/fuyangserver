from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

from users.models import User


class PictureTextColumn(models.Model):
    name = models.CharField('图文栏目名称', max_length=256)
    introduce = models.TextField('栏目简介', default='')
    category = models.CharField('所属类别', max_length=50, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图文栏目'
        verbose_name_plural = '图文栏目'
        ordering = ['pk']


class PictureTextPaper(models.Model):
    name = models.CharField('图文标题', max_length=256)
    column = models.ForeignKey(PictureTextColumn, on_delete=models.CASCADE, blank=True, verbose_name='所属栏目')
    remark = models.CharField('说明', max_length=256, blank=True, default='')  # 新增字段:用于标明课程价格、时长
    introduce = models.TextField('图文简介', default='')
    image = models.ImageField('封面', upload_to='image')
    register_date = models.DateTimeField('发表时间', default=timezone.now, editable=False)
    content = UEditorField('图文内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    views_count = models.IntegerField('浏览次数', default=0, editable=False)

    def __str__(self):
        return self.name

    def get_comment_count(self):
        return len(PictureTextPaperComment.objects.filter(ascription=self))

    class Meta:
        verbose_name = '图文文章'
        verbose_name_plural = '图文文章'


class PictureTextPaperComment(models.Model):
    message = models.CharField('图文评论', max_length=256)
    ascription = models.ForeignKey(PictureTextPaper, on_delete=models.CASCADE, blank=True, verbose_name='所属图文')
    register_date = models.DateTimeField('评论时间', auto_now_add=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='作者')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = '图文评论'
        verbose_name_plural = '图文评论'
        ordering = ['-register_date']
