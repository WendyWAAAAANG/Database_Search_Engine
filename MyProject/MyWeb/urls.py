"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#前台管理子路由文件

from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from MyWeb.views import shop,index,make

admin.autodiscover()

urlpatterns = [
  #  path('', index.login, name = 'LoginPage'),
  #   path('login', index.login, name="MyAdmin_login"),
  #   path('dologin', index.dologin, name="MyAdmin_dologin"),
  #   path('regist', index.regist, name="MyAdmin_regist"),
  #   path('LoginPage',index.login,name='LoginPage'),
  #   path('SigninPage',index.regist,name='SigninPage'),
  # #  path('Shop',index.Shop,name='Shop'),
  #   path('OnlineInquiry',index.OnlineInquiry,name='OnlineInquiry'),
  #   path('demo',index.demo,name='demo'),
  #   path('index',index.index,name='index'),
  #   path('Shop_family',index.Shop_family,name='Shop_family'),
  #   path('Shop_2',index.Shop_2,name='Shop_2'),
  #   path('Shop_3',index.Shop_3,name='Shop_3'),
  #   path('Shop_4',index.Shop_4,name='Shop_4'),
  #   path('Shop_5',index.Shop_5,name='Shop_5'),
  #   path('Shop_6',index.Shop_6,name='Shop_6'),
  #   path('Yishi',index.Yishi,name='Yishi'),
  #   path('AppointmentInfo',index.AppointmentInfo,name='AppointmentInfo'),
  #   path('Announcement',index.Announcement,name='Announcement'),
    #path('search/',search)

    path('', index.login, name = 'LoginPage'),
    path('demo',index.demo,name='demo'),
    path('SigninPage',index.regist,name='SigninPage'),
    path('Yishi',index.Yishi,name='Yishi'),

    path('Announcement',make.Announcement,name='Announcement'),
    path('OnlineInquiry/<int:pIndex>',make.OnlineInquiry,name='OnlineInquiry'),
    path('AppointmentInfo/<int:pIndex>',make.AppointmentInfo,name='AppointmentInfo'),
    path('OnlineInquiry/sub', make.subAppointment, name="MyWeb_Appointment_sub"),
    path('AppointmentInfo/toExamine', make.toExamine, name="MyWeb_Appointment_toExamine"),
    path('<int:pIndex>',index.Shop_list,name="Shop_list"),
    path('Shop/<int:pIndex>', shop.index, name="MyWeb_shop_index"),
    path('Visualization',index.Visualization,name="Visualization"),
    # path('Shop',index.Shop,name="Shop")
]

