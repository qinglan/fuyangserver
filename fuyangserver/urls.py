"""fuyangserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from study import views as study_views  # new

from userinfo import urls as userinfo_urls  # new
from django.conf import settings
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf.urls import include, url

urlpatterns = [
    path('', study_views.index),  # new
    path('admin/', admin.site.urls),

    path('yinanzazheng/', study_views.yinanzazheng),
    path('login/', study_views.do_login),
    path('register/', study_views.register),
    path('password/reset/', study_views.password_reset),
    path('weixin_check_signature/', study_views.weixin_check_signature),
    path('accounts/login/', study_views.weixin_login),
    path('weixin/redirect/', study_views.weixin_redirect, name='weixin_redirect'),

    path('MP_verify_9OqPDvvikphMdXB2.txt', study_views.mp_verify),
    path('MP_verify_SjPP8XG0lmvxzlAs.txt', study_views.MP_verify_SjPP8XG0lmvxzlAs),

    path('MP_verify_svvmO8SYa47rm2Sm.txt', study_views.MP_verify_svvmO8SYa47rm2Sm),

    path('videocurriculum/collection/<int:pk>/', study_views.video_curriculum_collection, name='video_curriculum_collection'),

    path('videocurriculum/<int:pk>/', study_views.video_curriculum_detail, name='video_curriculum_detail'),
    path('videocurriculumtasks/<int:pk>/', study_views.video_curriculum_tasks, name='video_curriculum_tasks'),
    path('videocurriculumtmaterial/<int:pk>/', study_views.video_curriculum_material, name='video_curriculum_material'),

    path('videocurriculumreviews/<int:pk>/', study_views.video_curriculum_reviews, name='video_curriculum_reviews'),
    path('videocurriculumreviews/curriculum/<int:pk>/', study_views.video_curriculum_reviews_curriculum, \
         name='video_curriculum_reviews_curriculum'),

    path('graphicarticle/<int:pk>/', study_views.graphic_article, name='graphic_article'),

    path('testlive/', study_views.testlive, name='testlive'),

    path('tasklive/introduce/<int:pk>/', study_views.tasklive_introduce, name='tasklive_introduce'),

    path('tasklive/ask/<int:pk>/', study_views.tasklive_ask, name='tasklive_ask'),

    path('tasklive/reviews/<int:pk>/', study_views.tasklive_reviews, name='tasklive_reviews'),

    path('tasklive/introduce/iframe/<int:pk>/', study_views.iframe_tasklive_introduce, name='iframe_tasklive_introduce'),

    path('tasklive/introduce/iframe/nextimage/<int:pk>/', study_views.iframe_tasklive_introduce_nextimage,
         name='iframe_tasklive_introduce_nextimage'),

    path('tasklive/introduce/iframe/liveimage/<int:pk>/', study_views.iframe_tasklive_introduce_liveimage,
         name='iframe_tasklive_introduce_liveimage'),

    path('tasklive/ask/iframe/<int:pk>/', study_views.iframe_tasklive_ask, name='iframe_tasklive_ask'),

    path('tasklive/ask/iframe/post/<int:pk>/', \
         study_views.iframe_tasklive_ask_post, name='iframe_tasklive_ask_post'),


    path('tasklive/reviews/iframe/<int:pk>/', study_views.iframe_tasklive_reviews, name='iframe_tasklive_reviews'),

    path('tasklive/reviews/iframe/post/<int:pk>/', \
         study_views.iframe_tasklive_reviews_post, name='iframe_tasklive_reviews_post'),


    path('tasklive/material/iframe/<int:pk>/', study_views.iframe_tasklive_material, name='iframe_tasklive_material'),


    path('studyfuyang/', study_views.studyfuyang, name='studyfuyang'),
    path('videolecture/', study_views.videolecture, name='videolecture'),




    path('studyfuyang/videoplaystudyfuyang/collection/<int:pk>/', study_views.videoplaystudyfuyang_collection, name='videoplaystudyfuyang_collection'),

    path('videolecture/videoplaylecture/collection/<int:pk>/', study_views.videoplaylecture_collection, name='videoplaylecture_collection'),


    path('studyfuyang/videoplaystudyfuyang/<int:pk>/', study_views.videoplaystudyfuyang, name='videoplaystudyfuyang'),

    path('videolecture/videoplaylecture/<int:pk>/', study_views.videoplaylecture, name='videoplaylecture'),

    path('studyfuyang/videoplaystudyfuyang/comment/<int:pk>/', study_views.videoplaystudyfuyang_comment, name='videoplaystudyfuyang_comment'),

    path('videolecture/videoplaylecture/comment/<int:pk>/', study_views.videoplaylecture_comment, name='videoplaylecture_comment'),

    path('buyvideolecture/<int:pk>/', study_views.buyvideolecture, name='buyvideolecture'),

    path('buystudyfuyang/<int:pk>/', study_views.buystudyfuyang, name='buystudyfuyang'),

    path('buyvideocurriculum/', study_views.buyvideocurriculum, name='buyvideocurriculum'),


    path('filedownload/<int:pk>/', study_views.big_file_download, name='big_file_download'),

    path('class/job/<int:pk>/', study_views.class_job, name='class_job'),

    path('class/job/redo/<int:pk>/', study_views.class_job_redo, name='class_job_redo'),

    path('class/job/iframe/<int:pk>/', study_views.class_job_iframe, name='class_job_iframe'),

    path('class/job/iframe/post/<int:pk>/', study_views.class_job_iframe_post, name='class_job_iframe_post'),

    #userinfo

    #url(r'^userinfo/', include('userinfo.urls')),
    path('userinfo/', include('userinfo.urls')),

    path('picture/text/', include('PictureText.urls')),

    url(r'^ueditor/', include('DjangoUeditor.urls')),




]



 
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)