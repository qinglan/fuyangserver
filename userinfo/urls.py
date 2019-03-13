from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

from userinfo import views

urlpatterns = [

    path('center/', views.userinfo_center, name='userinfo_center'),

    path('center/change/', views.userinfo_center_change, name='userinfo_center_change'),

    path('orders/', views.userinfo_orders, name='userinfo_orders'),

    path('orders/invoice/<int:pk>/', views.userinfo_orders_invoice, name='userinfo_orders_invoice'),

    path('orders/inner/', views.userinfo_orders_inner, name='userinfo_orders_inner'),

    path('invoice/', views.userinfo_invoice, name='userinfo_invoice'),

    path('invoice/cannel/', views.userinfo_invoice_cannel, name='userinfo_invoice_cannel'),

    path('collection/', views.userinfo_collection, name='userinfo_collection'),

    path('secure/', views.secure, name='userinfo_secure'),
    path('setpay/', views.pay_password, name='userinfo_setpay'),
    path('resetpass/', views.reset_password, name='userinfo_reset'),
    path('setmobile/', views.bind_mobile, name='userinfo_setmobile'),
    path('realname/', views.realname, name='userinfo_realname'),
    path('finance/', views.finance, name='userinfo_finance'),
    path('sendsms/', views.sendsms, name='userinfo_sendsms')
]
