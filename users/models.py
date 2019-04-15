from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from .managers import UserInheritanceManager, UserManager


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    USERS_AUTO_ACTIVATE = not settings.USERS_VERIFY_EMAIL

    email = models.CharField(
        _('user name'), max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(
        _('active'), default=USERS_AUTO_ACTIVATE,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, editable=False)

    objects = UserInheritanceManager()
    base_objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('用户管理')
        verbose_name_plural = _('用户管理')
        abstract = True

    def get_full_name(self):
        """ Return the email."""
        return self.email

    def get_short_name(self):
        """ Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])

    def activate(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.user_type_id:
            self.user_type = ContentType.objects.get_for_model(self, for_concrete_model=False)
        super(AbstractUser, self).save(*args, **kwargs)


class User(AbstractUser):
    """
    Concrete class of AbstractUser.
    Use this if you don't need to extend User.
    """
    openid = models.CharField('微信ID', default='', max_length=256)
    nickname = models.CharField('昵称', default='', max_length=256)
    sex = models.IntegerField('性别', default=1)
    province = models.CharField('省', default='', max_length=256)

    country = models.CharField('国', default='中国', max_length=256)

    headimgurl = models.CharField('头像URL',
                                  default='http://thirdwx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/46',
                                  max_length=1024)

    real_name = models.CharField('真实姓名', default='', max_length=256)

    phone_number = models.CharField('电话号码', default='',null=True, blank=True,  max_length=256)

    city = models.CharField('城市', default='', max_length=256)

    qq = models.CharField('QQ', max_length=50, default='')

    address = models.CharField('地址', default='', max_length=256)

    email_address = models.EmailField('邮箱', default='', max_length=256)

    paycode = models.CharField('支付密码', default='', max_length=50)

    idnum = models.CharField('身份证号', default='', max_length=50)
    idfront = models.ImageField('身份证正面', null=True, blank=True, upload_to='idcards')
    idback = models.ImageField('身份证反面', null=True, blank=True, upload_to='idcards')
    TYPE_CHOICE = (
        (u'0', u'未审核'),
        (u'1', u'审核中'),
        (u'2', u'审核通过'),
    )
    id_checkstate = models.CharField('身份证审核结果', max_length=2, choices=TYPE_CHOICE, default='0')

    account_sum = models.IntegerField('账户余额', default=0)
    attendance_ticket = models.IntegerField('听课券', default=0)
    exchange_ticket = models.IntegerField('兑换券', default=0)

    video_vip = models.IntegerField('视频区会员', choices=((0, u'非视频区VIP'), (1, u'视频区VIP')), default=0)

    def __str__(self):
        return self.nickname

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def is_realname(self):
        '是否实名认证'
        return self.real_name and self.idnum and self.idfront and self.idback


from users.models import User


class UserPaydetails(models.Model):
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='购买者')
    pay_bill = models.IntegerField('消费金额', default=0)

    TYPE_CHOICE = (
        (u'0', u'账户余额'),
        (u'1', u'听课券'),
        (u'2', u'兑换券'),
    )
    pay_type = models.CharField('消费分类', max_length=2, choices=TYPE_CHOICE, default='0')
    pay_date = models.DateTimeField('消费时间', default=timezone.now, editable=False)
    # pay_date = models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='消费时间'),
    remark = models.CharField('备注', default='', max_length=256, blank=True)

    class Meta:
        verbose_name = 'S用户消费记录单'
        verbose_name_plural = 'S用户消费记录单'
        ordering = ['-pay_date']
