from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

from PictureText import views

urlpatterns = [



    path('paper/<int:pk>/', views.picture_text_paper, name='picture_text_paper'),

    path('paper/comment/<int:pk>/', views.picture_text_paper_comment, name='picture_text_paper_comment'),

    path('column/<int:pk>/', views.picture_text_column, name='picture_text_column'),

]
