from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import random

# Create your views here.
from MyAdmin.models import category
def index(request, pIndex = 1):
    '''browse info'''
    cmod = category.objects
    clist = cmod.filter(cStatus__lt = 9)
    print(clist)
    mywhere = []
    context = {'categorylist': clist}

    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询种类编号或种类名称中只要含有关键字的都可以
        clist = clist.filter(Q(cName__contains = kw) | Q(id__contains = kw))
        mywhere.append("keyword=" + kw)

    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        clist = clist.filter(cStatus=status)
        mywhere.append("status=" + status)

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(clist, 10)  # 以5条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表

    # list2 = User.objects.all() #获取所有信息
    # 封装信息加载模板输出
    context = {"categorylist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "MyAdmin/Category/index.html", context)

def add(request):
                    #"""loading info, add into form"""
    return render(request,"MyAdmin/Category/add.html")

def insert(request):
    """conduct info inserting"""
    try:
        ob = category()
        #ob = category.objects.get(id=id)
        ob.cName = request.POST['cName']
        ob.cStatus = request.POST['cStatus']
        #ob.cStatus = 1
        ob.cCreate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.cUpdate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context={"info":"Successfully Added!"}
    except Exception as err:
        print(err)
        context={"info":"Failed to Add!"}
    return render(request,"MyAdmin/info.html",context)


def delete(request, id = 0):
    '''delete info'''
    try:
        ob = category.objects.get(id = id)
        ob.cStatus = 9
        ob.cUpdate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "Successfully Deleted!"}
    except Exception as err:
        print(err)
        context = {'info': "Failed to Delete!"}
    return render(request, "MyAdmin/info.html", context)

def edit(request, id = 0):
    '''edit info'''
    try:
        ob = category.objects.get(id = id)
        context = {'category': ob}
        return render(request, "MyAdmin/Category/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "Failed to Find Info for Editing!"}
        return render(request, "MyAdmin/info.html", context)

def update(request, id = 0):
    '''conduct info inserting'''
    try:
        ob = category.objects.get(id = id)
        ob.cName = request.POST['cName']
        #ob.cStatus = request.POST['cStatus']
        ob.cUpdate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "Successfully Updated!"}
    except Exception as err:
        print(err)
        context = {'info': "Failed to Update!"}
    return render(request, "MyAdmin/info.html", context)



