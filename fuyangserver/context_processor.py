#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-31 14:26:26
# @Author  : Weizhong Tu (mail@tuweizhong.com)

from django.conf import settings as original_settings
from users.models import User
from study.models import MianInfo,VideoCurriculum

def user_info(request):
    if request.user.is_authenticated:
        return {'user_info': dict(nickname=request.user.nickname, headimgurl=request.user.headimgurl)}
    else:
        return {'user_info': dict(nickname='匿名', \
                                  headimgurl='http://thirdwx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/46')}


def main_info(request):
    main_infos = MianInfo.objects.all();
    main_vcs = VideoCurriculum.objects.all()
    if len(main_infos) > 0:
        return {'main_info': main_infos[0],'main_vcs':main_vcs}

    return {'main_info':{},'main_vcs':main_vcs}
