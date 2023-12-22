from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Q
import time,os


from MyWeb.models import Drug,Category

def index(request,pIndex=1):
    '''浏览信息'''
    smod = Drug.objects
    mywhere={'search': '', 'type':''}
    # list = smod.filter(dStatus__lt=9)
    list = smod.filter()
    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("search",None)
    category = request.GET.get("category",None)
    if kw:
        list = list.filter(Q(name__icontains = kw) | Q(id__exact = kw))
        mywhere['search'] = kw
    if category:
        list = list.filter(type__exact = category)
        mywhere['type'] = category
    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list,28) #以8条每页创建分页对象
    maxpages = page.num_pages #最大页数
    #判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #当前页数据
    plist = page.page_range   #页码数列表
    #封装信息加载模板输出
    cmod = Category.objects
    clist = cmod.filter(cStatus__lt=9)
    context = {'categorylist': clist,"productlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"MyTemp/Shop/index.html",context)

def Shop_family(request):
    return render(request, 'Shop_family.html')

def Shop_2(request):
    return render(request,'Shop_2.html')

def Shop_3(request):
    return render(request,'Shop_3.html')

def Shop_4(request):
    return render(request,'Shop_4.html')

def Shop_5(request):
    return render(request,'Shop_5.html')

def Shop_6(request):
    return render(request,'Shop_6.html')
