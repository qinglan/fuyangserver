#!/usr/bin/env python
#
# def application(env, start_response):
#     start_response('200 OK', [('Content-Type','text/html')])
#     return [b"Hello World"] # python3


# 短信应用SDK AppID
appid = 1400190626  # SDK AppID是1400开头

# 短信应用SDK AppKey
appkey = "a2e88702d03c9f2453d33ea48bd86219"

# 需要发送短信的手机号码
phone_numbers = ["18938022656", "18666139171"]

# 短信模板ID，需要在短信应用中申请
template_id = 291365  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
# templateId 7839 对应的内容是"您的验证码是: {1}"
# 签名
sms_sign = "国医传承医学研究院"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台申请。

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import random

rndlist = random.sample('1234567890', 4)
rndnum = ''.join(rndlist)

ssender = SmsSingleSender(appid, appkey)
params = [rndnum]  # 短信验证码
try:
    result = ssender.send_with_param(86, phone_numbers[0], template_id, params, sign=sms_sign, extend="",
                                     ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
