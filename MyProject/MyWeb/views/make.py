from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect # add import with HttpResonseRedirect
from datetime import datetime
from django.http import JsonResponse
from MyWeb.models import Muser,Apothecary,Record
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

def OnlineInquiry(request,pIndex=1):
    smod = Apothecary.objects
    mywhere = []
    list = smod.filter()
    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询店铺名称中只要含有关键字就可以
        list = list.filter(name__contains=kw)
        mywhere.append("keyword=" + kw)
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 8)  # 以8条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表
    # 封装信息加载模板输出
    context = {"User_Appointment": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, 'MyTemp/Make/OnlineInquiry.html',context)

@csrf_exempt
def subAppointment(request):
    try:
        if request.COOKIES["uType"] == 'User':
            itemData = request.GET
            ob = Record()
            ob.aID = itemData['id']
            ob.uID = request.COOKIES["uId"]
            ob.addDate = itemData['date']
            ob.addTime = itemData['time']
            ob.addDepartment = itemData['aField']
            ob.addResult = '待审核'
            ob.createAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.updateAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()
            context = {"info": "Successfully Added!"}
        else:
            context = {'info': "Failed to commit!"}
    except Exception as err:
        print(err)
        context = {'info': "Failed to commit!"}
    return JsonResponse(context)

def AppointmentInfo(request,pIndex=1):
    smod = Record.objects
    list = smod.filter()
    aID = request.COOKIES["uId"]
    list = list.filter(aID__exact=aID)
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 8)  # 以8条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表
    # 封装信息加载模板输出
    context = {"record": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages}
    return render(request, "MyTemp/Make/AppointmentInfo.html",context)


def Announcement(request):
    return render(request, 'MyTemp/Make/Announcement.html')

def toExamine(request):
    try:
        if request.COOKIES["uType"] == 'Apothecary':
            itemData = request.GET
            aID = request.COOKIES["uId"]
            id = itemData["id"]
            print(itemData)
            ob = Record.objects.get(id=id)
            print(ob)
            ob.addResult = itemData['result']
            ob.updateAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ob.save()
            context = {"info": "Successfully update!"}
        else:
            context = {'info': "Failed to update!"}
    except Exception as err:
        print(err)
        context = {'info': "Failed to update!"}
    return JsonResponse(context)
