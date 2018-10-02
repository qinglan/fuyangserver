# coding:utf-8
from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from fuyangserver.settings import HERE
from fuyangserver.settings import MEDIA_URL
from study.models import AdvertisingBanners, VideoInfoLectureBanners, VideoInfoStudyFuyangBanners, TaskLiveFile
from study.models import VideoColumn
from study.models import VideoCurriculum
from study.models import VideoCurriculumComment
import xml.dom.minidom

from study.models import GraphicArticle
from study.models import VideoClass
from study.models import CurriculumTaskInfoVideo
from study.models import CurriculumTaskInfoJob
from study.models import VideoInfoLecture, VideoInfoLectureComment
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
import hashlib
import urllib.parse
import datetime
from django.utils import timezone
import time
import urllib

from userinfo.models import VideoCurriculumOrder
from userinfo.models import VideoInfoLectureOrder
from userinfo.models import VideoInfoStudyFuyangOrder
from django.db.models import Q
from django import forms

import urllib.request
import json
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.


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
    # return render(request, 'study/index.html')
    # logging.warning(request.user.username)
    # logging.warning(request.user)
    # logging.warning(request.user.user_permissions)
    # logging.warning(request.user.has_perm('blog.delete_article'))
    abs = AdvertisingBanners.objects.all()
    vcs = VideoCurriculum.objects.all().order_by('sequeue')
    # if len(vcs) > 0: return video_curriculum_detail(request, vcs[0].pk)

    return render(request, 'study/index.html', {'abs': abs, 'vcs': vcs})


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
    vc, comment_count, nowtime, isBuy, isCollection = video_curriculum_getinfo(request, pk)
    if vc is None:
        return HttpResponse('error')
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
                   'vccs': vccs,
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
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])

    maxpage = int((len(VideoInfoStudyFuyang.objects.all()) - 1) / PAGE_HAS_VIDEO) + 1
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

    vis = VideoInfoStudyFuyang.objects.all().order_by('sequeue')[
          page * PAGE_HAS_VIDEO - PAGE_HAS_VIDEO:page * PAGE_HAS_VIDEO]
    abs = VideoInfoStudyFuyangBanners.objects.all()
    return render(request, 'study/study_fuyang.html', \
                  {'vis': vis, \
                   'abs': abs, \
                   'maxleft': maxleft, 'left': left, 'maxright': maxright, 'right': right, \
                   'pagelist': pagelist})


@login_required(login_url='/accounts/login/')
def videolecture(request):
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])

    maxpage = int((len(VideoInfoLecture.objects.all()) - 1) / PAGE_HAS_VIDEO) + 1
    if page < 1:
        page = 1
    if page > maxpage:
        page = maxpage

    maxleft = reverse('videolecture') + '?page=1'

    left = reverse('videolecture') + '?page=' + str(page - 1)

    maxright = reverse('videolecture') + '?page=' + str(maxpage)

    right = reverse('videolecture') + '?page=' + str(page + 1)

    pagelist = []

    start = page - 1
    if start < 1:
        start = 1
    stop = start + 3
    if stop > maxpage + 1:
        stop = maxpage + 1

    for j in range(start, stop):
        itme = {}
        itme['url'] = reverse('videolecture') + '?page=' + str(j)
        itme['text'] = str(j)
        if j == page:
            itme['class'] = 'active'
        else:
            itme['class'] = ''
        pagelist.append(itme)

    vis = VideoInfoLecture.objects.all().order_by('sequeue')[
          page * PAGE_HAS_VIDEO - PAGE_HAS_VIDEO:page * PAGE_HAS_VIDEO]
    abs = VideoInfoLectureBanners.objects.all()
    return render(request, 'study/video_lecture.html', \
                  {'vis': vis, \
                   'abs': abs, \
                   'maxleft': maxleft, 'left': left, 'maxright': maxright, 'right': right, \
                   'pagelist': pagelist})


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
    gas = VideoInfoLecture.objects.filter(pk=pk)
    if len(gas) <= 0:
        return HttpResponse('error')
    gas[0].views_count = gas[0].views_count + 1
    gas[0].save()

    vpcs = VideoInfoLectureComment.objects.filter(ascription__pk=pk)

    us = VideoInfoLectureOrder.objects.filter(video__pk=pk)
    b = False
    for u in us:
        if u.purchaser.pk == request.user.pk:
            b = True
            break
    isBuy = gas[0].price == 0 or b

    # isCollection = Collection.is_collection(request.user, gas[0])
    return render(request, 'study/video_play_lecture.html', {'videoinfo': gas[0],
                                                             'isBuy': isBuy,
                                                             'vpcs': vpcs,
                                                             'isCollection': None})


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


def testlive(request):
    liveinfos = CurriculumTaskInfoVideo.objects.all()
    if len(liveinfos) <= 0:
        return HttpResponse('error')

    return render(request, 'study/testlive.html', {'liveinfo': liveinfos[0]})


@login_required(login_url='/accounts/login/')
def tasklive_introduce(request, pk):
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return HttpResponse('error')
    s = str(liveinfos[0].introduce)

    return render(request, 'study/tasklive_introduce.html', {'liveinfo': liveinfos[0]})


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
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return HttpResponse('error')

    s = str(liveinfos[0].introduce).replace("&nbsp;", '')
    timelist = liveinfos[0].image_show_time.split('.')
    if liveinfos[0].image_show_time == '':
        timelist = []
    xs = "<images>" + s + "</images>"
    domt = xml.dom.minidom.parseString(xs)

    imgs = domt.documentElement.getElementsByTagName("img")
    imageUrls = []
    if len(timelist) > 0:
        startTime = int(timelist[0])
        for (image, time) in zip(imgs, timelist):
            if image.hasAttribute("src"):
                i = {}
                i["src"] = image.getAttribute("src")
                i["time"] = int(time) - startTime
                imageUrls.append(i)

    return render(request, 'study/iframe_tasklive_introduce.html', \
                  {'liveinfo': liveinfos[0], 'imageUrls': imageUrls, \
                   'is_superuser': request.user.is_superuser})


def iframe_tasklive_introduce_nextimage(request, pk):
    liveinfos = CurriculumTaskInfoVideo.objects.filter(pk=pk)
    if len(liveinfos) <= 0:
        return HttpResponse('error')

    s = str(liveinfos[0].introduce)
    xs = "<images>" + s + "</images>"
    domt = xml.dom.minidom.parseString(xs)

    imgs = domt.documentElement.getElementsByTagName("img")

    timelist = liveinfos[0].image_show_time.split('.')
    if liveinfos[0].image_show_time == '':
        timelist = []

    if len(imgs) > len(timelist):
        liveinfos[0].live_image = imgs[len(timelist)].getAttribute("src")
        nowtime = timezone.now()
        s = str(int(time.mktime(nowtime.timetuple())))
        timelist.append(s)
        liveinfos[0].image_show_time = '.'.join(timelist)
        liveinfos[0].save()

    return HttpResponse('1')


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
        return HttpResponse('error')

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
    vcs = VideoInfoLecture.objects.filter(pk=pk)
    if len(vcs) > 0:
        order = VideoInfoLectureOrder.objects.create(
            price=vcs[0].price,
            purchaser=request.user,
            video=vcs[0],
        )
        order.save()

    return HttpResponse('1')


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
