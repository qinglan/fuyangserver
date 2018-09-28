from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
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

    phone_number = models.CharField('电话号码', default='', max_length=256)

    city = models.CharField('城市', default='', max_length=256)

    address = models.CharField('地址', default='', max_length=256)

    email_address = models.EmailField('邮箱', default='', max_length=256)

    def __str__(self):
        return self.nickname

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
