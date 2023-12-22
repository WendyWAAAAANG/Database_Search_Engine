#会员信息视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import random

from MyAdmin.models import Member

# ==============后台会员信息管理======================
# 浏览会员信息
def index(request, pIndex=1):

    mmod = Member.objects
    mlist = mmod.filter(id__gt=0)
    #mlist = mmod
    context = {'memberlist': mlist}

    #mlist = mmod.filter(uGender__contains ='f')
    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(mlist,6) #以5条每页创建分页对象
    maxpages = page.num_pages #最大页数
    #判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #当前页数据
    plist = page.page_range   #页码数列表

    #封装信息加载模板输出
    context = {"memberlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages}
    return render(request,"MyAdmin/Member/index.html",context)

def delete(request, id = 0):
    '''delete info'''
    try:
        ob = Member.objects.get(id = id)
        #ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "Successfully Deleted!"}
    except Exception as err:
        print(err)
        context = {'info': "Failed to Delete!"}
    return render(request, "MyAdmin/info.html", context)


## 还有在前台对用户的注册，数据库在后台已建立。