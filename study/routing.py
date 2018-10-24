# -*- coding:utf-8 -*-
# !/usr/bin/env python3
'''路由'''
__author__ = 'zween'
__mtime__ = '2018-10-22'

from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_id>\d+)/$', consumers.LivingRoomConsumer),
]
