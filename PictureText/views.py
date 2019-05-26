from django.http import HttpResponse
from django.shortcuts import render
from .models import PictureTextColumn, PictureTextPaper, PictureTextPaperComment
from advertise.models import VideoInfoLectureBanners
from study.models import VideoCurriculum, VideoVipPrice
from userinfo.models import VideoCurriculumOrder
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .paysettings import *
import json
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/accounts/login/')
def picture_text_paper(request, pk):
    abs = VideoInfoLectureBanners.objects.all()
    pp = PictureTextPaper.objects.get(pk=pk)
    pp.views_count += 1
    pp.save()
    comments = PictureTextPaperComment.objects.filter(ascription=pp)

    return render(request, 'PictureText/paper.html', {
        'paper': pp,
        'abs': abs,
        'comments': comments
    })


@login_required(login_url='/accounts/login/')
def picture_text_column(request, pk):
    '报名区'
    categories = PictureTextColumn.objects.filter(category='报名区').values('id', 'name').order_by('id')  # 获取报名区的所有类别
    curr_cate = PictureTextColumn.objects.filter(pk=pk).first()  # 获取当前栏目类别
    abs = VideoInfoLectureBanners.objects.all()  # banner广告
    papers = PictureTextPaper.objects.filter(column__pk=pk).order_by('-id')

    return render(request, 'PictureText/column.html', {
        'categories': categories,
        'column': curr_cate,
        'abs': abs,
        'papers': papers
    })


def picture_text_category(request, pk):
    '新增栏目：扶阳显议、医案辨析、天天乐、扶阳国医馆'
    abs = VideoInfoLectureBanners.objects.all()
    papers = PictureTextPaper.objects.filter(column__pk=pk).order_by('-id')
    if any(papers):
        catename = papers.first().column.category
        columns = PictureTextColumn.objects.filter(category=catename).order_by('id')  # 返回类别列表
        column = {}
        fs = PictureTextColumn.objects.filter(pk=pk)
        if len(fs) > 0: column = fs[0]

        return render(request, 'PictureText/category.html',
                      {'columns': columns, 'column': column, 'abs': abs, 'papers': papers})
    else:
        return render(request, 'PictureText/category.html', {'abs': abs})


def picture_text_details(request, pk):
    '新增栏目的详情页面'
    abs = VideoInfoLectureBanners.objects.all()
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/details.html', {'paper': papers[0], 'abs': abs, 'comments': comments})
    return HttpResponse('error')


def picture_text_paper_comment(request, pk):
    if request.method == 'POST':
        new_chat = PictureTextPaperComment.objects.create(
            message=request.POST.get('content'),
            ascription=PictureTextPaper.objects.get(pk=pk),
            author=request.user)

        new_chat.save()

    return HttpResponseRedirect(reverse('picture_text_paper', args=(pk,)))


def signpay(request, pk):
    '报名区在线支付'
    vc = VideoCurriculum.objects.get(pk=pk)
    return render(request, 'PictureText/signpay.html', locals())


def payment(request, vcid):
    '报名区在线支付'
    # vcid = request.GET.get('id')
    vc = VideoCurriculum.objects.get(pk=vcid)

    total_fee = vc.price
    if total_fee == 0: total_fee = 1
    total_fee *= 100
    getInfo = request.GET.get('getInfo', None)
    openid = request.COOKIES.get('openid', '')
    attachdict = {'action': 'baoming', 'cid': vcid, 'pt': 'wxpay', 'uid': request.user.pk}  # 附加数据，回调时原样返回

    if not openid:
        if getInfo != 'yes':
            # 构造一个url，携带一个重定向的路由参数，
            # 然后访问微信的一个url,微信会回调你设置的重定向路由，并携带code参数
            return HttpResponseRedirect(get_redirect_url(request.path))
        elif getInfo == 'yes':
            # 我设置的重定向路由还是回到这个函数中，其中设置了一个getInfo=yes的参数
            # 获取用户的openid
            openid = get_openid(request.GET.get('code'), request.GET.get('state', ''))

            if not openid: return HttpResponse('获取用户openid失败')

            response = render(request, 'PictureText/payment.html', {
                'params': get_jsapi_params(openid, total_fee, userdata=json.dumps(attachdict)),
                'vc': vc,
            })
            response.set_cookie('openid', openid, expires=60 * 60 * 24 * 30)
            return response
        else:
            return HttpResponse('获取机器编码失败')
    return render(request, 'PictureText/payment.html', {
        'params': get_jsapi_params(openid, total_fee, userdata=json.dumps(attachdict)),
        'vc': vc,
    })


def courseattent(request):
    '课程报名支付'
    pkid = int(request.GET['pk'])
    paytype = request.GET['pt']
    content = __saveorder(uid=request.user.pk, pk=pkid, pt=paytype)
    return HttpResponse(content)


@csrf_exempt
def checkwxorder(request):
    '检查微信订单是否成功'
    order_result = request.body
    xmldata = trans_xml_to_dict(order_result)
    print('xmlstr:', order_result)
    print('xmldata:', xmldata)
    if xmldata['return_code'] == 'SUCCESS' and xmldata['result_code'] == 'SUCCESS':
        userdata = json.loads(xmldata['attach'])
        print('userdata:', userdata)
        if userdata['action'] == 'baoming':  # 在线报名
            info = __saveorder(uid=userdata['uid'], pk=userdata['cid'], pt='wxpay')
        elif userdata['action'] == 'buyvideo':  # 购买视频
            from study.views import __saveorder as savevideoorder
            info = savevideoorder(userdata['uid'], pk=userdata['vid'], pt='wxpay')
        else:  # 账号充值
            info = 'other action todo'
        print('response data:', info)

    params = {
        'return_code': 'SUCCESS',
        'return_msg': 'OK'
    }
    return HttpResponse(trans_dict_to_xml(params))


def __saveorder(uid, pk, pt):
    '保存订单'
    from django.db import transaction
    from users.models import UserPaydetails, User
    pkid = int(pk)
    print('ss01:', pkid, 'userid:', uid)
    vc = VideoCurriculum.objects.get(pk=pkid)
    activeuser = User.objects.get(pk=uid)

    try:
        qs = VideoCurriculumOrder.objects.filter(price=vc.price, purchaser=activeuser, video_curriculum=vc)
        if qs.count() > 0: return '1'

        with transaction.atomic():
            order = VideoCurriculumOrder.objects.create(
                price=vc.price,
                purchaser=activeuser,
                video_curriculum=vc,
            )
            order.save()
            paytype = pt
            print('ss02:', paytype)

            if paytype == 'cashpay':
                activeuser.account_sum -= vc.price  # 账户余额扣减
                activeuser.save()
                UserPaydetails.objects.create(purchaser=activeuser,
                                              pay_bill=0 - vc.price,
                                              pay_type='0',
                                              remark='直播课程报名扣减余额')
                print('ss03:', '直播课程报名扣减余额')
            elif paytype == 'wxpay':
                vp = VideoVipPrice.objects.first()
                if vc.price >= vp.min_exchange_ticket_price:  # 当充值金额大于设置价格的时候才赠送兑换券
                    activeuser.exchange_ticket += vc.price  # 增加兑换券
                    activeuser.save()
                    UserPaydetails.objects.create(purchaser=activeuser,
                                                  pay_bill=0 + vc.price,
                                                  pay_type='2',
                                                  remark='直播课程报名赠送兑换券')
                    print('ss04:', '直播课程报名赠送兑换券')
                else:
                    print('直播课程报名成功但不赠送兑换券', vc.price, vp.min_exchange_ticket_price, activeuser.nickname)
            else:
                activeuser.attendance_ticket -= vc.price  # 听课券扣减
                activeuser.save()
                UserPaydetails.objects.create(purchaser=activeuser,
                                              pay_bill=0 - vc.price,
                                              pay_type='1',
                                              remark='直播课程报名扣减听课券')
                print('ss05:', '直播课程报名扣减听课券')
            print('ss06:return 1')
            return '1'
    except Exception as e:
        raise ValueError(e) from e
