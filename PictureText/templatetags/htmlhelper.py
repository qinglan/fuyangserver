# -*- coding:utf-8 -*-
# !/usr/bin/env python3
'''过虑器'''
__author__ = 'zween'
__mtime__ = '2018/12/3'
from django import template
from django.utils.safestring import mark_safe
from userinfo.models import VideoCurriculumOrder, VideoCurriculum
import datetime

register = template.Library()


@register.simple_tag
def is_buy(vid, uid):
    us = VideoCurriculumOrder.objects.filter(video_curriculum__pk=vid)

    isbuy = False;

    for u in us:
        if u.purchaser.pk == uid:
            alink = "<a href='javascript:void(0)'>已购买</a>"
            isbuy = True
            break

    if not isbuy:
        if us.first().video_curriculum.buy_time > datetime.datetime.now():
            alink = '<a href="javascript:void(0)" onclick="javascript:callpay(%d);return false">报名中</a>' % vid
        else:
            alink = "<a href='javascript:void(0)'>报名已截止</a>"

    return mark_safe(alink)
