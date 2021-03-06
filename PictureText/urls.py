from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

from PictureText import views

urlpatterns = [
    path('paper/<int:pk>/', views.picture_text_paper, name='picture_text_paper'),
    path('details/<int:pk>/', views.picture_text_details, name='picture_details'),
    path('paper/comment/<int:pk>/', views.picture_text_paper_comment, name='picture_text_paper_comment'),
    path('column/<int:pk>/', views.picture_text_column, name='picture_text_column'),
    path('category/<int:pk>/', views.picture_text_category, name='picture_text_category'),
    path('signpay/<int:pk>/', views.signpay, name='picture_text_signpay'),
    path('payment/<int:vcid>/', views.payment, name='picture_text_payment'),
    path('courseattent/', views.courseattent, name='picture_text_coursepay'),
    path('checkorder', views.checkwxorder, name='picture_text_checkorder')
]
