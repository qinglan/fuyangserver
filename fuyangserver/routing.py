# -*- coding:utf-8 -*-
# !/usr/bin/env python3
'''根路由'''
__author__ = 'zween'
__mtime__ = '2018-10-22'

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import study.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            study.routing.websocket_urlpatterns
        )
    ),
})
