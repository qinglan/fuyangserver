# coding:utf-8
from django.shortcuts import render
import os
from PictureText.models import PictureTextPaper
from fuyangserver.settings import HERE
from advertise.models import AdvertisingBanners, VideoInfoLectureBanners, VideoInfoStudyFuyangBanners
from study.models import VideoColumn
from study.models import VideoCurriculum
from study.models import VideoCurriculumComment
import xml.dom.minidom

from study.models import GraphicArticle
from study.models import VideoClass
from study.models import CurriculumTaskInfoVideo
from study.models import DataLst, SinglePage
from study.models import VideoInfoLecture, VideoInfoLectureComment, VideoInfoLectureClassfy
from study.models import VideoInfoStudyFuyang, VideoInfoStudyFuyangComment
from study.models import TaskInfoVideoComment
from study.models import TaskInfoVideoAsk
from study.models import VideoCurriculumFile
from study.models import TaskLiveFile
from study.models import CurriculumTaskInfoJob, CurriculumTaskInfoJobAnswer
from userinfo.models import Collection
from django.http import StreamingHttpResponse
from .comment_form import VideoCurriculumCommentForm, VideoInfoStudyFuyangCommentForm, VideoInfoLectureCommentForm
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import User
import urllib.parse
import datetime
import string, random
import urllib

from userinfo.models import VideoCurriculumOrder
from userinfo.models import VideoInfoLectureOrder
from userinfo.models import VideoInfoStudyFuyangOrder
import urllib.request
import json
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from PictureText.paysettings import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.csrf import csrf_exempt

'''
WEIXIN_APP_ID = 'wxb4bfb462ce44afd4'
WEIXIN_APPSECRET = '4488c166e2b78d2549b2a1ea56b8fa3e'
DO_MAIN = 'http://192.168.0.201'
'''
'''
WEIXIN_APP_ID = 'wx1024f1b772692562'
WEIXIN_APPSECRET = 'b99cf0e2eef5b8b1e8fbca5ec55f09ae'
DO_MAIN = 'http://fuyang.fengchewl.com'
'''

WEIXIN_APP_ID = 'wx6ce6cc38ff2c028c'
WEIXIN_APPSECRET = 'f8930880edce3dcf0039539e08074d5a'
DO_MAIN = 'http://fuyang.51nayun.com/'


@login_required(login_url='/accounts/login/')
def index(request):
    abs = VideoInfoLectureBanners.objects.all()  # banner广告
    items = PictureTextPaper.objects.filter(column_id=1, buy_time__gt=datetime.datetime.now()).order_by('sequeue')

    return render(request, 'study/index.html', locals())


def do_login(request):
    '''logging.warning(request.user.is_authenticated)

    logging.warning(request.user.username)
    logging.warning(request.user)
    logging.warning(request.user.user_permissions)

    logging.warning(request.user.has_perm('blog.delete_article'))
    logging.warning(request.user.user_permissions.add('blog.delete_article'))

    #request.uesr.auth.add_permission('blog.delete_article')
    user = authenticate(request, username='branch', password='t66y123456')
    if user is not None:
        if user.is_active:
            login(request, user)'''

    return render(request, 'study/login.html')


def weixin_login(request):
    next = request.GET['next']
    top = 'https://open.weixin.qq.com/connect/oauth2/authorize'

    u = DO_MAIN + reverse('weixin_redirect')
    redirect_uri = urllib.parse.quote_plus(u)
    url = top + '?appid=' + WEIXIN_APP_ID + '&redirect_uri=' + redirect_uri + \
          '&response_type=code&scope=snsapi_userinfo&state=' + \
          next + '#wechat_redirect'
    print(redirect_uri)
    return HttpResponseRedirect(url)


def loginByWeixin(infoDict, request):
    openid = infoDict['openid'];
    filterResult = User.objects.filter(openid=infoDict['openid'])
    if len(filterResult) > 0:
        user = filterResult[0]
        if not user.is_active:
            user.activate()
        login(request, user)
    else:
        user = User.objects.create(email=openid, password=openid)
        user.openid = openid
        user.nickname = infoDict.get('nickname', '')
        user.sex = infoDict.get('sex', 1)
        user.province = infoDict.get('province', '')
        user.country = infoDict.get('country', '')
        user.headimgurl = infoDict.get('headimgurl', '')

        user.save()
        if user.is_active:
            login(request, user)
    return True


def weixin_redirect(request):
    code = request.GET['code']
    next = request.GET['state']

    turl = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid='
    url = turl + WEIXIN_APP_ID + '&secret=' + WEIXIN_APPSECRET + '&code=' + code + '&grant_type=authorization_code'
    data = urllib.request.urlopen(url).read()

    record = data.decode('UTF-8')
    js = json.loads(record)

    if 'openid' in js:
        logging.warning('********openid:' + js['openid'])
    if 'errcode' in js:
        logging.error('********errcode:' + js['errcode'])

    logging.warning('********:' + record)
    logging.warning('********next:' + next)
    if ('openid' in js and 'access_token' in js):
        infoUrl = 'https://api.weixin.qq.com/sns/userinfo?access_token=' + js['access_token'] + \
                  '&openid=' + js['openid'] + '&lang=zh_CN'
        infodata = urllib.request.urlopen(infoUrl).read()
        infoDict = json.loads(infodata.decode('UTF-8'))
        logging.warning('********infodata:' + json.dumps(infoDict))
        if 'errcode' in js:
            logging.error('********errcode:' + js['errcode'])
            return HttpResponse('登录失败，请联系管理员')
        else:
            if loginByWeixin(infoDict, request):
                return HttpResponseRedirect(next)
            else:
                return HttpResponse('登录失败，请联系管理员')

    else:
        logging.error('登录失败')
        return HttpResponse('登录失败，请联系管理员')


@login_required(login_url='/accounts/login/')
def register(request):
    return render(request, 'study/register.html')


@login_required(login_url='/accounts/login/')
def password_reset(request):
    return render(request, 'study/password_reset.html')


@login_required(login_url='/accounts/login/')
def yinanzazheng(request):
    '疑难杂症'
    abs = AdvertisingBanners.objects.all()
    vcs = VideoColumn.objects.all()[0:2]
    return render(request, 'study/yinanzazheng.html', {'abs': abs, 'vcs': vcs})


def mp_verify(request):
    return render(request, 'study/MP_verify_9OqPDvvikphMdXB2.txt')


def MP_verify_SjPP8XG0lmvxzlAs(request):
    return render(request, 'study/MP_verify_SjPP8XG0lmvxzlAs.txt')


def MP_verify_svvmO8SYa47rm2Sm(request):
    return render(request, 'study/MP_verify_svvmO8SYa47rm2Sm.txt')


def weixin_check_signature(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = 'fuyangzhongyi'

        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        print('[token, timestamp, nonce]', hashlist)
        hashstr = ''.join([s for s in hashlist]).encode('utf-8')  # 这里必须增加encode('utf-8'),否则会报错
        print('hashstr befor sha1：', hashstr)
        hashstr = hashlib.sha1(hashstr).hexdigest()
        print('hashstr sha1:', hashstr)
        print('signature :', signature)
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('error')
    else:
        return HttpResponse('chenggong')


def video_curriculum_getinfo(request, pk):
    vcs = VideoCurriculum.objects.filter(pk=pk)
    if len(vcs) <= 0:
        return None, None, None, None, None
    isCollection = Collection.is_collection(request.user, vcs[0])
    comment_count = len(VideoCurriculumComment.objects.filter(ascription=vcs[0]))
    us = VideoCurriculumOrder.objects.filter(video_curriculum__pk=pk)

    isBuy = False
    for u in us:
        if u.purchaser.pk == request.user.pk:
            isBuy = True
            break
    return vcs[0], comment_count, datetime.datetime.now(), isBuy, isCollection


@login_required(login_url='/accounts/login/')
def video_curriculum_detail(request, pk):
    '直播详情页面'
    vc, comment_count, nowtime, isBuy, isCollection = video_curriculum_getinfo(request, pk)
    if vc is None:
        return HttpResponse('error')
    vc.views_count += 1
    vc.save()
    return render(request, 'study/video_curriculum_detail.html', {'vc': vc,
                                                                  'comment_count': comment_count,
                                                                  'nowtime': nowtime,
                                                                  'isBuy': isBuy,
                                                                  'isCollection': isCollection})


def video_curriculum_collection(request, pk):
    vcs = VideoCurriculum.objects.filter(pk=pk)
    if len(vcs) > 0:
        if 'is_save' in request.GET:
            Collection.save_collection(request.user, vcs[0])
            return HttpResponse('1')
        else:
            Collection.cancel_collection(request.user, vcs[0])
            return HttpResponse('1')
    return HttpResponse('error')


@login_required(login_url='/accounts/login/')
def video_curriculum_tasks(request, pk):
    '直播页面目录链接'
    vc, comment_count, nowtime, isBuy, isCollection = video_curriculum_getinfo(request, pk)
    if vc is None:
        return HttpResponse('error')
    classs = VideoClass.objects.filter(video_curriculum=vc).order_by("pub_date")
    datas = []
    for c in classs:
        task = {}
        task['class'] = c
        vs = CurriculumTaskInfoVideo.objects.filter(video_class=c).order_by('pub_date')
        task['vs'] = vs
        js = CurriculumTaskInfoJob.objects.filter(video_class=c).order_by('pub_date')
        task['js'] = js
        datas.append(task)

    return render(request, 'study/video_curriculum_tasks.html', {'vc': vc,
                                                                 'comment_count': comment_count,
                                                                 'datas': datas,
                                                                 'nowtime': nowtime,
                                                                 'isBuy': isBuy,
                                                                 'isCollection': isCollection})


@login_required(login_url='/accounts/login/')
def video_curriculum_material(request, pk):
    '直播：资料区'
    vc, comment_count, nowtime, isBuy, isCollection = video_curriculum_getinfo(request, pk)
    if vc is None:
        return HttpResponse('error')

    files = TaskLiveFile.objects.filter(ascription__video_curriculum=vc)

    return render(request, 'study/video_curriculum_material.html', {'vc': vc,
                                                                    'comment_count': comment_count,
                                                                    'files': files,
                                                                    'nowtime': nowtime,
                                                                    'isBuy': isBuy,
                                                                    'isCollection': isCollection})


PAGE_HAS_COMMENT = 20


@login_required(login_url='/accounts/login/')
def video_curriculum_reviews(request, pk):
    '直播详情页面评论'
    vc, comment_count, nowtime, isBuy, isCollection = video_curriculum_getinfo(request, pk)
    if vc is None:
        return HttpResponse('error')
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])

    maxpage = int((len(VideoCurriculumComment.objects.filter(ascription=vc)) - 1) / PAGE_HAS_COMMENT) + 1
    if page < 1:
        page = 1
    if page > maxpage:
        page = maxpage

    maxleft = reverse('video_curriculum_reviews', args=(pk,)) + '?page=1'

    left = reverse('video_curriculum_reviews', args=(pk,)) + '?page=' + str(page - 1)

    maxright = reverse('video_curriculum_reviews', args=(pk,)) + '?page=' + str(maxpage)

    right = reverse('video_curriculum_reviews', args=(pk,)) + '?page=' + str(page + 1)

    pagelist = []

    start = page - 1
    if start < 1:
        start = 1
    stop = start + 3
    if stop > maxpage + 1:
        stop = maxpage + 1

    for j in range(start, stop):
        itme = {}
        itme['url'] = reverse('video_curriculum_reviews', args=(pk,)) + '?page=' + str(j)
        itme['text'] = str(j)
        if j == page:
            itme['class'] = 'active'
        else:
            itme['class'] = ''
        pagelist.append(itme)

    vccs = VideoCurriculumComment.objects.filter(ascription=vc).order_by('-register_date')[
           page * PAGE_HAS_COMMENT - PAGE_HAS_COMMENT:page * PAGE_HAS_COMMENT]

    return render(request,
                  'study/video_curriculum_reviews.html',
                  {'vc': vc,
                   'comment_count': comment_count,
                   'nowtime': nowtime,
                   'isBuy': isBuy,
                   'isCollection': isCollection,
                   'vccs': vccs, 'maxleft': maxleft, 'left': left, 'maxright': maxright, 'right': right,
                   'pagelist': pagelist
                   })


def video_curriculum_reviews_curriculum(request, pk):
    vcs = VideoCurriculum.objects.filter(pk=pk)
    if len(vcs) <= 0:
        return HttpResponse('error')

    if request.method == 'POST':  # 当提交表单时
        form = VideoCurriculumCommentForm(request.POST)
        if form.is_valid():
            data = form.clean()
            content = data['content']
            score = data['score']
            VideoCurriculumComment.objects.create(message=content, ascription=vcs[0], \
                                                  author=request.user, score=score)
            form.clean()
            return HttpResponseRedirect(vcs[0].get_reviews_url())
    return HttpResponse('error')
    # return render(request, 'study/graphicarticle.html', {'ga': gas[0]})


def graphic_article(request, pk):
    gas = GraphicArticle.objects.filter(pk=pk)
    if len(gas) <= 0:
        return HttpResponse('error')
    return render(request, 'study/graphicarticle.html', {'ga': gas[0]})


PAGE_HAS_VIDEO = 18


@login_required(login_url='/accounts/login/')
def studyfuyang(request):
    '直播区首页'
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])

    maxpage = int((len(VideoCurriculum.objects.all()) - 1) / PAGE_HAS_VIDEO) + 1
    if page < 1:
        page = 1
    if page > maxpage:
        page = maxpage

    maxleft = reverse('studyfuyang') + '?page=1'

    left = reverse('studyfuyang') + '?page=' + str(page - 1)

    maxright = reverse('studyfuyang') + '?page=' + str(maxpage)

    right = reverse('studyfuyang') + '?page=' + str(page + 1)

    pagelist = []

    start = page - 1
    if start < 1:
        start = 1
    stop = start + 3
    if stop > maxpage + 1:
        stop = maxpage + 1

    for j in range(start, stop):
        itme = {}
        itme['url'] = reverse('studyfuyang') + '?page=' + str(j)
        itme['text'] = str(j)
        if j == page:
            itme['class'] = 'active'
        else:
            itme['class'] = ''
        pagelist.append(itme)

    vis = VideoCurriculum.objects.filter(is_show=True).order_by('sequeue')[
          page * PAGE_HAS_VIDEO - PAGE_HAS_VIDEO:page * PAGE_HAS_VIDEO]
    abs = VideoInfoStudyFuyangBanners.objects.all()
    return render(request, 'study/study_fuyang.html', \
                  {'vis': vis, \
                   'abs': abs, \
                   'maxleft': maxleft, 'left': left, 'maxright': maxright, 'right': right, \
                   'pagelist': pagelist})


@login_required(login_url='/accounts/login/')
def studyfuyang_index(request):
    '直播区首页样式改版'
    items = VideoCurriculum.objects.filter(is_show=True).order_by('sequeue')
    abs = VideoInfoStudyFuyangBanners.objects.all()
    return render(request, 'study/studyfuyang_index.html', locals())


@login_required(login_url='/accounts/login/')
def videolecture(request):
    '视频区首页'
    vcls = VideoInfoLectureClassfy.objects.all().order_by('sequeue')
    return render(request, 'study/video_lecture.html', locals())


def videocates(request, cid):
    '视频区二级分类列表'
    vcls = VideoInfoLectureClassfy.objects.all().order_by('sequeue')
    tuijian = VideoInfoLecture.objects.filter(lecture_type_first__pk=cid, lecture_type_second='0').order_by('sequeue')[
              :4]
    zhibao = VideoInfoLecture.objects.filter(lecture_type_first__id=cid, lecture_type_second='1').order_by('sequeue')[
             :4]
    return render(request, 'study/video_secates.html', locals())


def videopages(request):
    '视频区栏目分页'
    cateid = int(request.GET.get('cid', '0'))
    flag = int(request.GET.get('flag', '0'))
    page = request.GET.get('page')
    txtkey = request.GET.get('txtkey', '')
    vcls = VideoInfoLectureClassfy.objects.all().order_by('sequeue')
    vlist = VideoInfoLecture.objects.all().order_by('sequeue')
    if cateid > 0:
        vlist = vlist.filter(lecture_type_first=cateid)
    if flag > 0:
        vlist = vlist.filter(lecture_type_second=flag)
    if len(txtkey) > 0:
        vlist = vlist.filter(name__icontains=txtkey)

    p = Paginator(vlist, 16)  # 每页显示16条数据
    try:
        pageInfo = p.page(page)
    except PageNotAnInteger:
        pageInfo = p.page(1)  # 如果参数page数据类型不是整数，就返回第一页数据
    except EmptyPage:
        pageInfo = p.page(p.num_pages)  # 若用户访问的页数大于实际页数，则返回最后一页数据
    return render(request, 'study/video_pages.html', locals())


def videoplaylecture_collection(request, pk):
    vcs = VideoInfoLecture.objects.filter(pk=pk)
    if len(vcs) > 0:
        if 'is_save' in request.GET:
            Collection.save_collection(request.user, vcs[0])
            return HttpResponse('1')
        else:
            Collection.cancel_collection(request.user, vcs[0])
            return HttpResponse('1')
    return HttpResponse('error')


def videoplaystudyfuyang_collection(request, pk):
    vcs = VideoInfoStudyFuyang.objects.filter(pk=pk)
    if len(vcs) > 0:
        if 'is_save' in request.GET:
            Collection.save_collection(request.user, vcs[0])
            return HttpResponse('1')
        else:
            Collection.cancel_collection(request.user, vcs[0])
            return HttpResponse('1')
    return HttpResponse('error')


@login_required(login_url='/accounts/login/')
def videoplaystudyfuyang(request, pk):
    gas = VideoInfoStudyFuyang.objects.filter(pk=pk)
    if len(gas) <= 0:
        return HttpResponse('error')
    gas[0].views_count = gas[0].views_count + 1
    gas[0].save()
    vpcs = VideoInfoStudyFuyangComment.objects.filter(ascription__pk=pk)
    us = VideoInfoStudyFuyangOrder.objects.filter(video__pk=pk)
    b = False
    for u in us:
        if u.purchaser.pk == request.user.pk:
            b = True
            break
    isBuy = gas[0].price == 0 or b
    isCollection = Collection.is_collection(request.user, gas[0])
    return render(request, 'study/video_play_studyfuyang.html', {'videoinfo': gas[0],
                                                                 'isBuy': isBuy,
                                                                 'vpcs': vpcs,
                                                                 'isCollection': isCollection})


@login_required(login_url='/accounts/login/')
def videoplaylecture(request, pk):
    '视频区详情页面'
    gas = VideoInfoLecture.objects.filter(pk=pk)
    if len(gas) <= 0: return HttpResponse('error')
    gas[0].views_count += 1
    gas[0].save()

    vpcs = VideoInfoLectureComment.objects.filter(ascription__pk=pk)  # 视频评论

    us = VideoInfoLectureOrder.objects.filter(video__pk=pk)
    b = False
    for u in us:
        if u.purchaser.pk == request.user.pk:
            b = True
            break
    isBuy = gas[0].price == 0 or b or request.user.video_vip == 1
    # isCollection = Collection.is_collection(request.user, gas[0])
    relations = VideoInfoLecture.objects.filter(lecture_type_first=gas[0].lecture_type_first,
                                                lecture_type_second=gas[0].lecture_type_second).order_by('-id')[:4]

    print('gas[0].price', gas[0].price)
    if gas[0].price == 0:
        gas[0].price = 1

    return render(request, 'study/video_play_lecture.html', {
        'videoinfo': gas[0],
        'isBuy': isBuy,
        'vpcs': vpcs,
        'relations': relations})


def paytype(request, pk):
    '视频区购买：支付方式'
    vc = VideoInfoLecture.objects.get(pk=pk)
    return render(request, 'study/paytype.html', locals())


def payment(request, vid):
    '视频区微信支付页面'
    # vid = request.GET.get('id')
    vc = VideoInfoLecture.objects.get(pk=vid)
    total_fee = vc.price * 100

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
            if not openid:
                return HttpResponse('获取用户openid失败')
            print('openid', openid)
            print('code', request.GET.get('code', ''))
            print('state', request.GET.get('state', ''))

            response = render(request, 'study/payment.html',
                              {'params': get_jsapi_params(openid, total_fee), 'videoinfo': vc})
            response.set_cookie('openid', openid, expires=60 * 60 * 24 * 30)
            return response

        else:
            return HttpResponse('获取机器编码失败')
    return render(request, 'study/payment.html', {
        'params': get_jsapi_params(openid, total_fee),
        'videoinfo': vc
    })


def videoplaylecture_comment(request, pk):
    vcs = VideoInfoLecture.objects.filter(pk=pk)
    if len(vcs) <= 0:
        return HttpResponse('error')

    if request.method == 'POST':  # 当提交表单时
        form = VideoInfoLectureCommentForm(request.POST)
        if form.is_valid():
            data = form.clean()
            content = data['content']
            VideoInfoLectureComment.objects.create(message=content, ascription=vcs[0], \
                                                   author=request.user)
            form.clean()
            return HttpResponseRedirect(vcs[0].get_absolute_url())
    return HttpResponse('error')


def videoplaystudyfuyang_comment(request, pk):
    vcs = VideoInfoStudyFuyang.objects.filter(pk=pk)
    if len(vcs) <= 0:
        return HttpResponse('error')

    if request.method == 'POST':  # 当提交表单时
        form = VideoInfoStudyFuyangCommentForm(request.POST)
        if form.is_valid():
            data = form.clean()
            content = data['content']
            VideoInfoStudyFuyangComment.objects.create(message=content, ascription=vcs[0], \
                                                       author=request.user)
            form.clean()
            return HttpResponseRedirect(vcs[0].get_absolute_url())
    return HttpResponse('error')


def guide(request, pk):
    '使用指南'
    zhinan = SinglePage.objects.filter(pk=pk)
    if any(zhinan):
        return render(request, 'study/guide.html', {'zhinan': zhinan.first()})
    else:
        return HttpResponse('参数有误：数据不存在')


def getdatalist(request):
    '资料区'
    abs = VideoInfoLectureBanners.objects.all()
    ds = DataLst.objects.all().order_by('-id')
    if any(ds):
        return render(request, 'study/datalist.html', {'ds': ds, 'abs': abs})
    else:
        return render(request, 'study/datalist.html', {'abs': abs})


def getdatadetail(request, pk):
    abs = VideoInfoLectureBanners.objects.all()
    ds = DataLst.objects.filter(pk=pk)
    if any(ds):
        return render(request, 'study/datadetail.html', {'item': ds.first(), 'abs': abs})
    else:
        return HttpResponse('没有数据')


def testlive(request):
    liveinfos = CurriculumTaskInfoVideo.objects.all()
    if len(liveinfos) <= 0:
        return HttpResponse('error')

    return render(request, 'study/testlive.html', {'liveinfo': liveinfos[0]})


@login_required(login_url='/accounts/login/')
def tasklive_introduce(request, pk):
    '直播详情页面'
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return HttpResponse('error')
    info = liveinfos.first()
    vid = info.video_class.video_curriculum_id  # 视频Id
    us = VideoCurriculumOrder.objects.filter(video_curriculum__pk=vid)
    isBuy = False
    for u in us:
        if u.purchaser.pk == request.user.pk:
            isBuy = True
            break

    if request.user.is_superuser or isBuy:  # 管理员和购买人才可能看视频
        return render(request, 'study/tasklive_introduce.html', {'liveinfo': info})
    return HttpResponse('您还未购买该课程')


def tasklive_ask(request, pk):
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return HttpResponse('error')

    return render(request, 'study/tasklive_ask.html', {'liveinfo': liveinfos[0]})


def tasklive_reviews(request, pk):
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return HttpResponse('error')

    return render(request, 'study/tasklive_reviews.html', {'liveinfo': liveinfos[0]})


def iframe_tasklive_introduce(request, pk):
    '直播详情页面：文档'
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0: return HttpResponse('error')

    s = str(liveinfos[0].introduce).replace("&nbsp;", '')
    timelist = liveinfos[0].image_show_time.split('.')
    if liveinfos[0].image_show_time == '': timelist = []
    xs = "<images>" + s + "</images>"
    domt = xml.dom.minidom.parseString(xs)

    imgs = domt.documentElement.getElementsByTagName("img")
    imageUrls = []
    for i in imgs:
        imageUrls.append(i.getAttribute('src'))
    # if len(timelist) > 0:
    #     startTime = int(timelist[0])
    #     for (image, time) in zip(imgs, timelist):
    #         if image.hasAttribute("src"):
    #             i = {}
    #             i["src"] = image.getAttribute("src")
    #             i["time"] = int(time) - startTime
    #             imageUrls.append(i)

    return render(request, 'study/iframe_tasklive_introduce.html', \
                  {'liveinfo': liveinfos[0], 'imageUrls': imageUrls, \
                   'is_superuser': request.user.is_superuser})


def iframe_tasklive_introduce_nextimage(request, pk):
    '直播详情页面：文档下一页'
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0: return HttpResponse('error')
    info = liveinfos.first()

    s = str(info.introduce)
    xs = "<images>" + s + "</images>"
    domt = xml.dom.minidom.parseString(xs)

    imgs = domt.documentElement.getElementsByTagName("img")
    n = int(request.GET.get('num', 1))
    if n >= len(imgs): n = n + 1 % len(imgs)

    return HttpResponse(imgs[n].getAttribute('src'))  # 默认返回第一张图片


def iframe_tasklive_introduce_liveimage(request, pk):
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return HttpResponse('')
    if liveinfos[0].live_image is None:
        return HttpResponse('')
    else:
        return HttpResponse(liveinfos[0].live_image)


def iframe_tasklive_ask(request, pk):
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return render(request, 'study/iframe_tasklive_ask.html')

    comments = TaskInfoVideoAsk.objects.filter(ascription__pk=pk)

    return render(request, 'study/iframe_tasklive_ask.html', {'liveinfo': liveinfos[0], 'comments': comments})


def iframe_tasklive_reviews(request, pk):
    '直播：讨论区'
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return render(request, 'study/iframe_tasklive_reviews.html')

    comments = TaskInfoVideoComment.objects.filter(ascription__pk=pk)

    return render(request, 'study/iframe_tasklive_reviews.html', {'liveinfo': liveinfos[0], 'comments': comments})


def iframe_tasklive_material(request, pk):
    files = TaskLiveFile.objects.filter(ascription=CurriculumTaskInfoVideo.objects.get(pk=pk).video_class)

    return render(request, 'study/iframe_tasklive_material.html', {'files': files})


def iframe_tasklive_reviews_post(request, pk):
    if request.method == 'POST':
        post_type = request.POST.get('post_type')
        if post_type == 'send_chat':
            liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
            if len(liveinfos) <= 0:
                return HttpResponse('error')
            new_chat = TaskInfoVideoComment.objects.create(
                message=request.POST.get('content'),
                ascription=liveinfos[0],
                author=request.user)
            new_chat.save()
            return HttpResponse()
        elif post_type == 'get_chat':
            last_chat_id = 0
            if 'last_chat_id' in request.POST:
                last_chat_id = int(request.POST.get('last_chat_id'))

            comments = TaskInfoVideoComment.objects.filter(id__gt=last_chat_id, ascription__pk=pk)
            return render(request, 'study/iframe_tasklive_reviews_list.html', \
                          {'comments': comments})
    else:
        return HttpResponse('error')


def iframe_tasklive_ask_post(request, pk):
    if request.method == 'POST':
        post_type = request.POST.get('post_type')
        if post_type == 'send_chat':
            liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
            if len(liveinfos) <= 0:
                return HttpResponse('error')
            new_chat = TaskInfoVideoAsk.objects.create(
                message=request.POST.get('content'),
                ascription=liveinfos[0],
                author=request.user)
            new_chat.save()
            return HttpResponse()
        elif post_type == 'get_chat':
            last_chat_id = 0
            if 'last_chat_id' in request.POST:
                last_chat_id = int(request.POST.get('last_chat_id'))

            comments = TaskInfoVideoAsk.objects.filter(id__gt=last_chat_id, ascription__pk=pk)
            return render(request, 'study/iframe_tasklive_ask_list.html', \
                          {'comments': comments})

    else:
        return HttpResponse('error')


def buyvideocurriculum(request):
    if 'pk' in request.GET:
        pkid = int(request.GET['pk'])
        vcs = VideoCurriculum.objects.filter(pk=pkid)
        if len(vcs) > 0:
            order = VideoCurriculumOrder.objects.create(
                price=vcs[0].price,
                purchaser=request.user,
                video_curriculum=vcs[0],
            )
            order.save()

    return HttpResponse('1')


def big_file_download(request, pk):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    files = VideoCurriculumFile.objects.filter(pk=pk)
    if len(files) > 0:

        the_file_name = files[0].file.url
        path = os.path.join(HERE, 'static')
        response = StreamingHttpResponse(file_iterator(the_file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

        return response
    else:
        return HttpResponse('error')


def class_job(request, pk):
    js = CurriculumTaskInfoJob.objects.filter(pk=pk)
    if len(js) <= 0:
        return HttpResponse('error')

    jas = CurriculumTaskInfoJobAnswer.objects.filter(author=request.user, job_parent=js[0])
    # 是否已回答
    if len(jas) <= 0:
        return render(request, 'study/class_job.html', {'job': js[0]})
    else:
        return render(request, 'study/class_job_answer.html', {'job': js[0], 'answer': jas[0]})


def class_job_iframe(request, pk):
    js = CurriculumTaskInfoJob.objects.filter(pk=pk)
    if len(js) <= 0:
        return HttpResponse('error')

    jas = CurriculumTaskInfoJobAnswer.objects.filter(author=request.user, job_parent=js[0])
    # 是否已回答
    if len(jas) <= 0:
        return render(request, 'study/iframe_class_job.html', {'job': js[0]})
    else:
        # return HttpResponse('error')
        return render(request, 'study/iframe_class_job.html')


def class_job_iframe_post(request, pk):
    if request.method == 'POST':
        post_type = request.POST.get('post_type')
        if post_type == 'send_chat':
            js = CurriculumTaskInfoJob.objects.filter(pk=pk)
            if len(js) <= 0:
                return HttpResponse('error')
            new_chat = CurriculumTaskInfoJobAnswer.objects.create(
                comment='',
                job_parent=js[0],
                job_content=request.POST.get('answer'),
                author=request.user)
            new_chat.save()

            return HttpResponse('error')

    else:
        return HttpResponse('error')


def class_job_redo(request, pk):
    js = CurriculumTaskInfoJob.objects.filter(pk=pk)
    if len(js) <= 0:
        return HttpResponse('error')

    CurriculumTaskInfoJobAnswer.objects.filter(author=request.user, job_parent=js[0]).delete()

    return HttpResponseRedirect(reverse('class_job', args=(pk,)))


def buyvideolecture(request, pk):
    '购买视频'
    from django.db import transaction
    from users.models import UserPaydetails
    try:
        with transaction.atomic():
            vcs = VideoInfoLecture.objects.get(pk=pk)
            paytype = request.GET.get('pt')
            if vcs:
                order = VideoInfoLectureOrder.objects.create(
                    price=vcs.price,
                    purchaser=request.user,
                    video=vcs,
                )
                order.save()

                if paytype == 'cashpay':
                    request.user.account_sum -= vcs.price  # 账户余额扣减
                    UserPaydetails.objects.create(purchaser=request.user,
                                                  pay_bill=0 - vcs.price,
                                                  pay_type='0',
                                                  remark='视频购买扣减余额')
                elif paytype == 'wxpay':
                    request.user.exchange_ticket += vcs.price  # 增加兑换券
                    UserPaydetails.objects.create(purchaser=request.user,
                                                  pay_bill=0 + vcs.price,
                                                  pay_type='2',
                                                  remark='视频购买赠送兑换券')
                else:
                    request.user.attendance_ticket -= vcs.price  # 听课券扣减
                    UserPaydetails.objects.create(purchaser=request.user,
                                                  pay_bill=0 - vcs.price,
                                                  pay_type='1',
                                                  remark='视频购买扣减听课券')

                request.user.save()
            return HttpResponse('1')
    except Exception as e:
        return HttpResponse("出现错误<%s>" % str(e))


def buystudyfuyang(request, pk):
    vcs = VideoInfoStudyFuyang.objects.filter(pk=pk)
    if len(vcs) > 0:
        order = VideoInfoStudyFuyangOrder.objects.create(
            price=vcs[0].price,
            purchaser=request.user,
            video=vcs[0],
        )
        order.save()

    return HttpResponse('1')


class wxsign(object):
    '获取微信签名'

    def __init__(self, url):
        self.ret = {
            'nonceStr': self.__create_nonce_str(),
            'timestamp': self.__create_timestamp(),
            'url': url,
        }
        self.__ticket()

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def __ticket(self):
        strurl = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
            WEIXIN_APP_ID, WEIXIN_APPSECRET)
        # self.ret['responseText'] = GetData(strurl)
        jsondata = json.loads(GetData(strurl))
        access_token = jsondata['access_token']
        # self.ret['access_token'] = access_token

        strurl = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&access_token=%s' % access_token
        jsondata = json.loads(GetData(strurl))
        self.ret['jsapi_ticket'] = jsondata['ticket']

    def getSign(self):
        string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        # print('check sign:', string)
        self.ret['signature'] = hashlib.sha1(string.encode()).hexdigest()
        self.ret['appId'] = WEIXIN_APP_ID
        return self.ret


def getwxsign(request):
    '获取微信签名'
    # url = '{0}://{1}{2}'.format(request.scheme.lower(), request.get_host(), request.get_full_path())
    # url = 'http://fuyang.51nayun.com/videolecture/videoplaylecture/25/'
    url = request.META.get('HTTP_REFERER')
    # print('share url:', url)
    wx = wxsign(url)
    wxdata = wx.getSign()
    return HttpResponse(json.dumps(wxdata))


def GetData(strurl):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    request = urllib.request.Request(strurl, headers=headers)
    import ssl
    context = ssl._create_unverified_context()
    res = urllib.request.urlopen(request, context=context)
    d = res.read().decode()
    return d
