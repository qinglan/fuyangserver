# -*- coding:utf-8 -*-
# !/usr/bin/env python3
'''过虑器'''
__author__ = 'zween'
__mtime__ = '2018/12/3'
from django import template
from django.utils.safestring import mark_safe
from userinfo.models import VideoCurriculumOrder

register = template.Library()


@register.simple_tag
def is_buy(vid, uid):
    us = VideoCurriculumOrder.objects.filter(video_curriculum__pk=vid)
    alink = '<a href="javascript:void(0)" onclick="javascript:callpay(%d);return false">立即报名</a>' % vid
    for u in us:
        if u.purchaser.pk == uid:
            alink = "<a href='javascript:void(0)'>已购买</a>"
            break
    return mark_safe(alink)
