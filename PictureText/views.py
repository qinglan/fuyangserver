from django.http import HttpResponse
from django.shortcuts import render
from .models import PictureTextColumn, PictureTextPaper, PictureTextPaperComment
from advertise.models import VideoInfoLectureBanners
from study.models import VideoCurriculum
from userinfo.models import VideoCurriculumOrder
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .paysettings import *


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


def payment(request, pk):
    '报名区在线支付'
    vc = VideoCurriculum.objects.get(pk=pk)

    total_fee = vc.price
    if total_fee == 0: total_fee = 1
    total_fee *= 100
    getInfo = request.GET.get('getInfo', None)
    openid = request.COOKIES.get('openid', '')
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
                'params': get_jsapi_params(openid, total_fee),
                'vc': vc,
            })
            response.set_cookie('openid', openid, expires=60 * 60 * 24 * 30)
            return response
        else:
            return HttpResponse('获取机器编码失败')
    return render(request, 'PictureText/payment.html', {
        'params': get_jsapi_params(openid, total_fee),
        'vc': vc,
    })


def courseattent(request):
    '课程报名支付'
    from django.db import transaction
    from users.models import UserPaydetails
    pkid = int(request.GET['pk'])
    vc = VideoCurriculum.objects.get(pk=pkid)

    try:
        with transaction.atomic():
            order = VideoCurriculumOrder.objects.create(
                price=vc.price,
                purchaser=request.user,
                video_curriculum=vc,
            )
            order.save()
            paytype = '0' if request.GET['pt'] in ['cashpay', 'wxpay'] else '1'
            UserPaydetails.objects.create(purchaser=request.user,
                                          pay_bill=0 - vc.price,
                                          pay_type=paytype,
                                          remark='直播课程报名')
            return HttpResponse('1')
    except Exception as e:
        return HttpResponse("出现错误<%s>" % str(e))
