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
    '课程页面判断是否购买课程'
    us = VideoCurriculumOrder.objects.filter(video_curriculum__pk=vid)

    isbuy = False

    for u in us:
        if u.purchaser.pk == uid:
            alink = "<a href='javascript:void(0)'>已购买</a>"
            isbuy = True
            break

    if not isbuy:
        vc = VideoCurriculum.objects.get(pk=vid)
        if vc.buy_time > datetime.datetime.now():
            alink = '<a href="javascript:checkpay(%d,%d,%d)">报名中</a>' % (vid, vc.price, int(vc.pay_type))
        else:
            alink = "<a href='javascript:void(0)'>报名已截止</a>"

    return mark_safe(alink)


@register.simple_tag
def index_check_buy(id, vid, uid):
    '首页判断是否购买课程过虑器'
    us = VideoCurriculumOrder.objects.filter(video_curriculum__pk=vid)

    isbuy = False

    for u in us:
        if u.purchaser.pk == uid:
            alink = "<a href='javascript:void(0)'>已购买</a>"
            isbuy = True
            break

    if not isbuy:
        vc = VideoCurriculum.objects.get(pk=vid)
        if vc.buy_time > datetime.datetime.now():
            alink = '<a href="/picture/text/paper/%s/">报名中</a>' % id
        else:
            alink = "<a href='javascript:void(0)'>报名已截止</a>"

    return mark_safe(alink)
