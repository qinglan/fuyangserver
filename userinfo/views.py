from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import VideoCurriculumOrder, VideoInfoStudyFuyangOrder, VideoInfoLectureOrder, Collection


def ordersSortKey(elem):
    return elem.register_date


def userinfo_center(request):
    return render(request, 'userinfo/center.html', {})


def userinfo_collection(request):
    collections = Collection.objects.filter(author=request.user)
    return render(request, 'userinfo/collection.html', {'collections': collections})


def userinfo_center_change(request):
    if request.method == 'POST':
        # request.user.country = request.POST.get('profile[title]')
        # request.user.province = request.POST.get('profile[signature]')
        request.user.nickname = request.POST.get('profile[truename]')
        request.user.sex = int(request.POST.get('profile[gender]'))
        # request.user.real_name = request.POST.get('profile[real_name]')
        # request.user.phone_number = request.POST.get('profile[phone_number]')
        # request.user.city = request.POST.get('profile[city]')
        request.user.qq = request.POST.get('profile[qq]')
        request.user.address = request.POST.get('profile[address]')
        request.user.email_address = request.POST.get('profile[email_address]')

        request.user.save()
        return HttpResponseRedirect(reverse('userinfo_center'))
    return HttpResponseRedirect(reverse('userinfo_center'))


def userinfo_orders(request):
    orders = []
    a = VideoCurriculumOrder.objects.filter(purchaser=request.user)
    b = VideoInfoStudyFuyangOrder.objects.filter(purchaser=request.user)
    c = VideoInfoLectureOrder.objects.filter(purchaser=request.user)
    orders.extend(a)
    orders.extend(b)
    orders.extend(c)
    orders.sort(key=ordersSortKey, reverse=True)
    return render(request, 'userinfo/orders.html', {'orders': orders})


def userinfo_invoice(request):
    orders = []
    a = VideoCurriculumOrder.objects.filter(purchaser=request.user, apply_bill=True)
    b = VideoInfoStudyFuyangOrder.objects.filter(purchaser=request.user, apply_bill=True)
    c = VideoInfoLectureOrder.objects.filter(purchaser=request.user, apply_bill=True)
    orders.extend(a)
    orders.extend(b)
    orders.extend(c)
    orders.sort(key=ordersSortKey, reverse=True)
    return render(request, 'userinfo/invoice.html', {'orders': orders})


def userinfo_invoice_cannel(request):
    if 'pk' in request.GET:
        pk = int(request.GET['pk'])
        order = get_order(pk)
        order.apply_bill = False
        order.save()
    return HttpResponse("1")


def userinfo_orders_inner(request):
    if 'pk' in request.GET:
        pk = int(request.GET['pk'])
        order = get_order(pk)
        if order is not None:
            return render(request, 'userinfo/orders_inner.html', {'order': order})
    return HttpResponse("")


def userinfo_orders_invoice(request, pk):
    if request.method == 'POST':
        headName = request.POST.get('headName')
        headType = request.POST.get('headType')
        invoiceSn = request.POST.get('invoiceSn')
        targetEmail = request.POST.get('targetEmail')
        tkc = request.POST.get('ticket')

        order = get_order(pk)

        if order is not None:
            order.taitou_type = headType
            order.taitou_text = headName
            order.recognition_id = invoiceSn
            order.email = targetEmail
            order.apply_bill = True
            order.ticket = tkc
            order.save()
            return HttpResponseRedirect(reverse('userinfo_orders'))

    return HttpResponseRedirect(reverse('userinfo_orders'))


def get_order(pk):
    orders = VideoCurriculumOrder.objects.filter(pk=pk)
    if len(orders) > 0:
        return orders[0]

    orders = VideoInfoStudyFuyangOrder.objects.filter(pk=pk)
    if len(orders) > 0:
        return orders[0]

    orders = VideoInfoLectureOrder.objects.filter(pk=pk)
    if len(orders) > 0:
        return orders[0]

    return None


def secure(request):
    '安全设置'
    if request.method == 'POST':
        request.user.phone_number = request.POST.get('profile[phone]')
        request.user.paycode = request.POST.get('profile[paycode]')
        request.user.save()
        return HttpResponseRedirect(reverse('userinfo_secure'))
    return render(request, 'userinfo/secure.html')


def pay_password(request):
    '设置支付密码'
    if request.method == 'POST':
        vcode = request.POST.get('sms_code')
        if vcode == request.session["smscode"]:
            request.user.paycode = request.POST.get('newPayPassword')  # todo:支付密码最好加密
            request.user.save()
            del request.session["smscode"]
            return HttpResponseRedirect(reverse('userinfo_secure'))
        else:
            render(request, 'userinfo/setpay.html', {'errmsg': '设置支付密码失败：验证码输入有误.'})
    return render(request, 'userinfo/setpay.html')


def reset_password(request):
    '重设支付密码'
    return render(request, 'userinfo/resetpay.html')


def bind_mobile(request):
    '设置手机号码'
    if request.method == 'POST':
        vcode = request.POST.get('sms_code')
        if vcode == request.session["smscode"]:
            request.user.phone_number = request.POST.get('mobile')
            request.user.save()
            del request.session["smscode"]
            return HttpResponseRedirect(reverse('userinfo_secure'))
        else:
            return render(request, 'userinfo/setmobile.html', {'errmsg': '绑定手机号码失败：验证码输入有误.'})
    return render(request, 'userinfo/setmobile.html')


def realname(request):
    '实名认证'
    if request.method == 'POST':
        request.user.real_name = request.POST.get('truename')
        request.user.idnum = request.POST.get('idcard')
        request.user.idfront = request.FILES.get('faceImg')
        request.user.idback = request.FILES.get('backImg')
        request.user.save()

        return HttpResponseRedirect(reverse('userinfo_realname'))
    return render(request, 'userinfo/realname.html')


def finance(request):
    '财务中心'
    return render(request, 'userinfo/finance.html')


@csrf_exempt
def sendsms(request):
    '发送短信验证码'

    # 短信应用SDK AppID
    appid = 1400190626  # SDK AppID是1400开头
    # 短信应用SDK AppKey
    appkey = "a2e88702d03c9f2453d33ea48bd86219"
    # 需要发送短信的手机号码
    phone_numbers = [request.POST.get('phone')]
    # 短信模板ID，需要在短信应用中申请
    template_id = 291365  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
    # templateId 7839 对应的内容是"您的验证码是: {1}"
    # 签名
    sms_sign = "国医传承医学研究院"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。

    from qcloudsms_py import SmsSingleSender
    from qcloudsms_py.httpclient import HTTPError
    import random

    ssender = SmsSingleSender(appid, appkey)
    rndlist = random.sample('1234567890', 4)
    rndnum = ''.join(rndlist)
    request.session['smscode'] = rndnum
    params = [rndnum]  # 短信验证码
    try:
        result = ssender.send_with_param(86, phone_numbers[0], template_id, params, sign=sms_sign, extend="",
                                         ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
    return JsonResponse(result)  # {'result': 0, 'errmsg': 'OK', 'ext': '', 'sid': '2019:3801938042322070546', 'fee': 1}
