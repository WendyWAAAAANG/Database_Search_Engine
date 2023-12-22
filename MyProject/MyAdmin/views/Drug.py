from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import time, os
import random

#Create your views here.
from MyAdmin.models import Drug, category
def index(request,pIndex=1):
    '''浏览信息'''
    smod = Drug.objects
    mywhere=[]
    alist = smod.filter(dStatus__lt=9)
    context = {'druglist':alist}

    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword",None)
    if kw:
        # 查询Drug Name中只要含有关键字就可以
        alist = alist.filter(Q(dName__contains = kw) | Q(id__exact = kw))
        mywhere.append("keyword="+kw)

    # 获取、判断并封装菜品类别category_id搜索条件
    # id = request.GET.get('category_id','')
    # if id != '':
    #     alist = alist.filter(category_id=id)
    #     mywhere.append("category_id="+id)

    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('dStatus','')
    if status != '':
        alist = alist.filter(dStatus=status)
        mywhere.append("status=" + status)

    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(alist,15) #以25条每页创建分页对象
    maxpages = page.num_pages #最大页数
    #判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #当前页数据
    plist = page.page_range   #页码数列表

    #封装信息加载模板输出
    context = {"productlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"MyAdmin/Drug/index.html",context)

def add(request):
    '''加载添加页面'''
    return render(request,"MyAdmin/Drug/add.html")

def insert(request):
    '''执行添加'''
    try:

        #实例化model，封装信息，并执行添加
        ob = Drug()
        #ob.id = request.POST['id']
        ob.dName = request.POST['dName']
        ob.dEffect = request.POST['dEffect']
        ob.dUsage = request.POST['dUsage']
        ob.dType = request.POST['dType']
        ob.dSale = request.POST['dSale']
        ob.dNum = request.POST['dNum']
        ob.dPrice = request.POST['dPrice']
        ob.dStatus = 1
        ob.dCreate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.dUpdate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context={"info":"Successfully Added!"}
    except Exception as err:
        print(err)
        context={"info":"Failed to Add!"}
    return render(request,"MyAdmin/info.html",context)

def delete(request,id = 0):
    '''删除信息'''
    try:
        ob = Drug.objects.get(id=id)
        ob.dStatus = 9
        ob.dUpdate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context={"info":"Successfully Deleted!"}
    except Exception as err:
        print(err)
        context={"info":"Failed to Delete!"}
    #return JsonResponse(context)
    return render(request,"MyAdmin/info.html",context)


def edit(request,id):
    '''加载编辑信息页面'''
    try:
        ob = Drug.objects.get(id = id)
        context={"Drug":ob}
        return render(request,"MyAdmin/Drug/edit.html",context)
    except Exception as err:
        print(err)
        context={"info":"Failed to Edit!"}
        return render(request,"MyAdmin/info.html",context)

def update(request,id):
    '''执行编辑信息'''
    try:

        ob = Drug.objects.get(id = id)
        ob.dName = request.POST['dName']
        ob.dEffect = request.POST['dEffect']
        ob.dUsage = request.POST['dUsage']
        ob.dType = request.POST['dType']
        ob.dSale = request.POST['dSale']
        ob.dNum = request.POST['dNum']
        ob.dPrice = request.POST['dPrice']
        ob.dStatus = request.POST['dStatus']
        ob.dUpdate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context={"info":"Successfully Updated!"}
    except Exception as err:
        print(err)
        context={"info":"Failed to Update!"}
    return render(request,"MyAdmin/info.html",context)