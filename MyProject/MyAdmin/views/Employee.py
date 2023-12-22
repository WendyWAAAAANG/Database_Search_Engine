from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import random
import time, os

# Create your views here.
from MyAdmin.models import Employee
def index(request, pIndex = 1):
    '''browse info'''
    emod = Employee.objects
    elist = emod.filter(status__lt = 9)
    #elist = emod
    mywhere = []
    context = {'userlist': elist}

    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询员工账号或姓名中只要含有关键字的都可以
        elist = elist.filter(Q(name__contains = kw) | Q(id__contains = kw))
        mywhere.append("keyword=" + kw)

    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        elist = elist.filter(status=status)
        mywhere.append("status=" + status)

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(elist, 5)  # 以5条每页创建分页对象
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
    context = {"userlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "MyAdmin/Employee/index.html", context)

def add(request):
    """loading info, add into form"""
    return render(request,"MyAdmin/Employee/add.html")

def insert(request):
    """conduct info inserting"""
    try:
        ob = Employee()
        ob.name = request.POST['name']
        ob.division = request.POST['division']
        ob.tel = request.POST['tel']
        # 将当前员工信息的密码做md5处理
        import hashlib, random
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password'] + str(n)  # 从表单中获取密码并添加干扰值???
        md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
        ob.password_hash = md5.hexdigest()  # 获取md5值
        ob.password_salt = n
        ob.status = request.POST['status']
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "Successfully Inserted!"}
    except Exception as err:
        print(err)
        context = {'info': "Failed to Insert!"}
    return render(request, "MyAdmin/info.html", context)

def delete(request, eid = 0):
    '''delete info'''
    try:
        ob = Employee.objects.get(id = eid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "Successfully Deleted!"}
    except Exception as err:
        print(err)
        context = {'info': "Failed to Delete!"}
    return render(request, "MyAdmin/info.html", context)

def edit(request, eid = 0):
    '''edit info'''
    try:
        ob = Employee.objects.get(id = eid)
        context = {'Employee': ob}
        #print("enter edit...")
        return render(request, "MyAdmin/Employee/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "Failed to Find Info for Editing!"}
        return render(request, "MyAdmin/info.html", context)

def update(request, eid = 0):
    '''conduct info inserting'''
    #print('enter update',eid)
    try:
        ob = Employee.objects.get(id = eid)
        #ob.name = request.POST['name']
        ob.status = request.POST['status']
        ob.tel = request.POST['tel']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "Successfully Updated!"}
    except Exception as err:
        print(err)
        context = {'info': "Failed to Update!"}
    return render(request, "MyAdmin/info.html", context)



"""
def resetpass(request,uid):
    '''加载重置会员密码信息页面'''
    try:
        ob = User.objects.get(id=uid)
        context={"user":ob}
        return render(request,"myadmin/user/resetpass.html",context)
    except Exception as err:
        context={"info":"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)

def doresetpass(request,uid):
    '''执行编辑信息'''
    try:
        ob = User.objects.get(id=uid)
        #获取密码并md5
        import hashlib
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password']+str(n) 
        md5.update(s.encode('utf-8'))
        ob.password_hash = md5.hexdigest()
        ob.password_salt = n
        ob.save()
        context={"info":"密码重置成功！"}
    except Exception as err:
        print(err)
        context={"info":"密码重置失败"}
    return render(request,"myadmin/info.html",context)
"""