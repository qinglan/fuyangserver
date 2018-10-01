from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

from PictureText import views

urlpatterns = [



    path('paper/<int:pk>/', views.picture_text_paper, name='picture_text_paper'),
    path('paper1/<int:pk>/', views.picture_text_paper1, name='picture_text_paper1'),
    path('paper2/<int:pk>/', views.picture_text_paper2, name='picture_text_paper2'),
    path('paper3/<int:pk>/', views.picture_text_paper3, name='picture_text_paper3'),
    path('paper4/<int:pk>/', views.picture_text_paper4, name='picture_text_paper4'),

    path('paper/comment/<int:pk>/', views.picture_text_paper_comment, name='picture_text_paper_comment'),
    path('paper/comment1/<int:pk>/', views.picture_text_paper_comment1, name='picture_text_paper_comment1'),
    path('paper/comment2/<int:pk>/', views.picture_text_paper_comment2, name='picture_text_paper_comment2'),
    path('paper/comment3/<int:pk>/', views.picture_text_paper_comment3, name='picture_text_paper_comment3'),
    path('paper/comment4/<int:pk>/', views.picture_text_paper_comment4, name='picture_text_paper_comment4'),

    path('column/<int:pk>/', views.picture_text_column, name='picture_text_column'),
    path('column1/<int:pk>/', views.picture_text_column1, name='picture_text_column1'),
    path('column2/<int:pk>/', views.picture_text_column2, name='picture_text_column2'),
    path('column3/<int:pk>/', views.picture_text_column3, name='picture_text_column3'),
    path('column4/<int:pk>/', views.picture_text_column4, name='picture_text_column4'),

]
