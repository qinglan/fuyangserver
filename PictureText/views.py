from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import PictureTextColumn, PictureTextPaper, PictureTextPaperComment
from advertise.models import VideoInfoLectureBanners
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .paysettings import *


def picture_text_paper(request, pk):
    abs = VideoInfoLectureBanners.objects.all()
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/paper.html', {'paper': papers[0], 'abs': abs, 'comments': comments})
    return HttpResponse('error')


def picture_text_column(request, pk):
    '报名区'
    categories = PictureTextColumn.objects.filter(category='报名区').values('id', 'name').order_by('id')  # 获取报名区的所有类别
    curr_cate = PictureTextColumn.objects.filter(pk=pk).first()  # 获取当前栏目类别
    papers = PictureTextPaper.objects.filter(column__pk=pk).order_by('-id')

    abs = VideoInfoLectureBanners.objects.all()  # banner广告

    total_fee = papers[0].video.price
    if total_fee == 0: total_fee = 1
    total_fee *= 100
    getInfo = request.GET.get('getInfo', None)
    openid = request.COOKIES.get('openid', '')
    if not openid:
        if getInfo != 'yes':
            # 构造一个url，携带一个重定向的路由参数，
            # 然后访问微信的一个url,微信会回调你设置的重定向路由，并携带code参数
            return HttpResponseRedirect(get_redirect_url())
        elif getInfo == 'yes':
            # 我设置的重定向路由还是回到这个函数中，其中设置了一个getInfo=yes的参数
            # 获取用户的openid
            openid = get_openid(request.GET.get('code'), request.GET.get('state', ''))
            if not openid:
                return HttpResponse('获取用户openid失败')
            print('openid', openid)
            print('code', request.GET.get('code', ''))
            print('state', request.GET.get('state', ''))

            response = render(request, 'PictureText/column.html', {
                'params': get_jsapi_params(openid, total_fee), 'categories': categories,
                'column': curr_cate, 'abs': abs, 'papers': papers})
            response.set_cookie('openid', openid, expires=60 * 60 * 24 * 30)
            return response
        else:
            return HttpResponse('获取机器编码失败')

    return render(request, 'PictureText/column.html', {
        'params': get_jsapi_params(openid, total_fee), 'categories': categories, 'column': curr_cate,
        'abs': abs, 'papers': papers})

    # return render(request, 'PictureText/column.html', {'categories': categories, 'column': curr_cate, 'abs': abs, 'papers': papers})


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

# class WxJsAPIPay(View):
#     def get(self, request, *args, **kwargs):
#         """
#         用户点击一个路由或者扫码进入这个views.py中的函数，首先获取用户的openid,
#         使用jsapi方式支付需要此参数
#         :param self:
#         :param request:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         getInfo = request.GET.get('getInfo', None)
#         openid = request.COOKIES.get('openid', '')
#         if not openid:
#             if getInfo != 'yes':
#                 # 构造一个url，携带一个重定向的路由参数，
#                 # 然后访问微信的一个url,微信会回调你设置的重定向路由，并携带code参数
#                 return HttpResponseRedirect(get_redirect_url())
#             elif getInfo == 'yes':
#                 # 我设置的重定向路由还是回到这个函数中，其中设置了一个getInfo=yes的参数
#                 # 获取用户的openid
#                 openid = get_openid(request.GET.get('code'), request.GET.get('state', ''))
#                 if not openid:
#                     return HttpResponse('获取用户openid失败')
#                 response = render_to_response('wx_js_pay.html', context={'params': get_jsapi_params(openid)})
#                 response.set_cookie('openid', openid, expires=60 * 60 * 24 * 30)
#                 return response
#
#             else:
#                 return HttpResponse('获取机器编码失败')
#         else:
#             return render(request, 'wx_js_pay.html', context={'params': get_jsapi_params(openid)})
