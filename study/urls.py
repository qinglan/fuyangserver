# -*- coding:utf-8 -*-
# !/usr/bin/env python3
''''''
__author__ = 'zween'
__mtime__ = '2019-04-07'

from django.urls import path
from .views import *

urlpatterns = [
    path('yinanzazheng/', yinanzazheng),
    path('videocurriculum/collection/<int:pk>/', video_curriculum_collection, name='video_curriculum_collection'),
    path('videocurriculum/<int:pk>/', video_curriculum_detail, name='video_curriculum_detail'),
    path('videocurriculumtasks/<int:pk>/', video_curriculum_tasks, name='video_curriculum_tasks'),
    path('videocurriculumtmaterial/<int:pk>/', video_curriculum_material, name='video_curriculum_material'),

    path('videocurriculumreviews/<int:pk>/', video_curriculum_reviews, name='video_curriculum_reviews'),
    path('videocurriculumreviews/curriculum/<int:pk>/', video_curriculum_reviews_curriculum, \
         name='video_curriculum_reviews_curriculum'),

    path('graphicarticle/<int:pk>/', graphic_article, name='graphic_article'),

    path('testlive/', testlive, name='testlive'),

    path('tasklive/introduce/<int:pk>/', tasklive_introduce, name='tasklive_introduce'),

    path('tasklive/ask/<int:pk>/', tasklive_ask, name='tasklive_ask'),

    path('tasklive/reviews/<int:pk>/', tasklive_reviews, name='tasklive_reviews'),

    path('tasklive/introduce/iframe/<int:pk>/', iframe_tasklive_introduce,
         name='iframe_tasklive_introduce'),

    path('tasklive/introduce/iframe/nextimage/<int:pk>/', iframe_tasklive_introduce_nextimage,
         name='iframe_tasklive_introduce_nextimage'),

    path('tasklive/introduce/iframe/liveimage/<int:pk>/', iframe_tasklive_introduce_liveimage,
         name='iframe_tasklive_introduce_liveimage'),

    path('tasklive/ask/iframe/<int:pk>/', iframe_tasklive_ask, name='iframe_tasklive_ask'),

    path('tasklive/ask/iframe/post/<int:pk>/', \
         iframe_tasklive_ask_post, name='iframe_tasklive_ask_post'),

    path('tasklive/reviews/iframe/<int:pk>/', iframe_tasklive_reviews, name='iframe_tasklive_reviews'),

    path('tasklive/reviews/iframe/post/<int:pk>/', \
         iframe_tasklive_reviews_post, name='iframe_tasklive_reviews_post'),

    path('tasklive/material/iframe/<int:pk>/', iframe_tasklive_material, name='iframe_tasklive_material'),

    path('studyfuyang/', studyfuyang_index, name='studyfuyang'),
    path('videolecture/', videolecture, name='videolecture'),

    path('videolectureindex/', videolectureindex, name='videolectureindex'),

    path('videolecture/videoplaylecture/<int:pk>/', videoplaylecture, name='videoplaylecture'),

    path('videolecture/category/<int:cid>', videocates, name='videocates'),
    path('videolecture/pagination/', videopages, name='video_pages'),

    path('singlepage/<int:pk>/', guide, name='guide'),
    path('datalist/', getdatalist, name='datalist'),
    path('datadetail/<int:pk>/', getdatadetail, name='datadetail'),

    path('studyfuyang/videoplaystudyfuyang/collection/<int:pk>/', videoplaystudyfuyang_collection,
         name='videoplaystudyfuyang_collection'),

    path('videolecture/videoplaylecture/collection/<int:pk>/', videoplaylecture_collection,
         name='videoplaylecture_collection'),

    path('studyfuyang/videoplaystudyfuyang/<int:pk>/', videoplaystudyfuyang, name='videoplaystudyfuyang'),

    path('studyfuyang/videoplaystudyfuyang/comment/<int:pk>/', videoplaystudyfuyang_comment,
         name='videoplaystudyfuyang_comment'),

    path('videolecture/videoplaylecture/comment/<int:pk>/', videoplaylecture_comment,
         name='videoplaylecture_comment'),

    path('paytype/<int:pk>/', paytype, name='study_paytype'),
    path('payment/<int:vid>/', payment, name='study_payment'),

    path('buyvideolecture/<int:pk>/', buyvideolecture, name='buyvideolecture'),

    path('buystudyfuyang/<int:pk>/', buystudyfuyang, name='buystudyfuyang'),

    path('buyvideocurriculum/', buyvideocurriculum, name='buyvideocurriculum'),

    path('filedownload/<int:pk>/', big_file_download, name='big_file_download'),

    path('class/job/<int:pk>/', class_job, name='class_job'),

    path('class/job/redo/<int:pk>/', class_job_redo, name='class_job_redo'),

    path('class/job/iframe/<int:pk>/', class_job_iframe, name='class_job_iframe'),

    path('class/job/iframe/post/<int:pk>/', class_job_iframe_post, name='class_job_iframe_post'),

]
