"""fuyangserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from study.views import index as study_index
from study.views import do_login, weixin_login, register, password_reset, weixin_check_signature, weixin_redirect, \
    mp_verify, MP_verify_SjPP8XG0lmvxzlAs, MP_verify_svvmO8SYa47rm2Sm, getwxsign

urlpatterns = [
    path('', study_index),  # new
    path('login/', do_login),
    path('accounts/login/', weixin_login),
    path('register/', register),
    path('password/reset/', password_reset),
    path('weixin_check_signature/', weixin_check_signature),
    path('weixin/redirect/', weixin_redirect, name='weixin_redirect'),

    path('MP_verify_9OqPDvvikphMdXB2.txt', mp_verify),
    path('MP_verify_SjPP8XG0lmvxzlAs.txt', MP_verify_SjPP8XG0lmvxzlAs),
    path('MP_verify_svvmO8SYa47rm2Sm.txt', MP_verify_svvmO8SYa47rm2Sm),
    path('wxsign/', getwxsign),

    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('study/', include('study.urls')),
    path('userinfo/', include('userinfo.urls')),
    path('picture/text/', include('PictureText.urls')),
    re_path(r'^ueditor/', include('DjangoUeditor.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
