from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
from MyWeb.models import Muser

class RegistUserForm(forms.Form):
    uName = forms.CharField(label = 'Username', max_length=10)
    uPassword = forms.CharField(label= 'Password', max_length=10, widget=forms.PasswordInput)
    uType = forms.CharField(label='UserType', max_length=10)
    uGender = forms.CharField(label = 'UserGender', max_length=6)
    uBirth = forms.CharField(label='UserBirth', max_length=8)
    uTel = forms.CharField(label='UserTel', max_length=11)
    uAddress = forms.CharField(label='UserAddress', max_length=30)

class LoginUserForm(forms.Form):
    uName = forms.CharField(label = 'Username', max_length=10)
    uPassword = forms.CharField(label= 'Password', max_length=10, widget=forms.PasswordInput)
    uType = forms.CharField(label='UserType', max_length=10)

#用户登录首页
def index(request):
    return render(request, 'MyTemp/Home/LoginPage.html')

def demo(request):
    return render(request, 'MyTemp/Home/demo.html')

def regist(request):
    if request.method == 'POST':
        userform = RegistUserForm(request.POST)
        if userform.is_valid():
            uName = userform.cleaned_data['uName']
            uPassword = userform.cleaned_data['uPassword']
            uType = userform.cleaned_data['uType']
            uGender = userform.cleaned_data['uGender']
            uBirth = userform.cleaned_data['uBirth']
            uTel = userform.cleaned_data['uTel']
            uAddress = userform.cleaned_data['uAddress']
            Muser.objects.create(uName=uName,uPassword=uPassword,uType=uType,uGender=uGender,uBirth=uBirth,uTel=uTel,uAddress=uAddress)
            Muser().save()
            return HttpResponseRedirect("/")
    else:
        userform = RegistUserForm()
    return render(request,'MyTemp/Home/SigninPage.html',{'userform':userform})

def login(request):
    if request.method == 'POST':
        userform = LoginUserForm(request.POST)
        if userform.is_valid():
            uName = userform.cleaned_data['uName']
            user1 = Muser.objects.filter(uName__exact=uName)
            if user1:
                uPassword = userform.cleaned_data['uPassword']
                uType = userform.cleaned_data['uType']
                user = Muser.objects.filter(uName__exact=uName, uPassword__exact=uPassword, uType__exact=uType).values('uId')
                if user:
                    print(user[0]['uId'])
                    if uType == "User":
                        response = render(request, 'MyTemp/Home/demo.html', {'userform': userform})
                        response.set_cookie('uId', user[0]['uId'])
                        response.set_cookie('uType', uType)
                        return response
                    elif uType == "Apothecary":
                        response = render(request, 'MyTemp/Home/Yishi.html', {'userform': userform})
                        response.set_cookie('uId', user[0]['uId'])
                        response.set_cookie('uType', uType)
                        return response
                    else:
                        return HttpResponse('Incorrect Type Information! Try Again!')
                else:
                    return HttpResponse('Incorrect Password! Try Again!')
            else:
                return HttpResponse('Account do not exist! Try Again!')
    else:
        userform = LoginUserForm()
    return render(request,'MyTemp/Home/LoginPage.html',{'userform':userform})


# def login(request):
#     if request.method == 'POST':
#         userform = LoginUserForm(request.POST)
#         if userform.is_valid():
#             uName = userform.cleaned_data['uName']
#             uPassword = userform.cleaned_data['uPassword']
#             uType = userform.cleaned_data['uType']
#             user = Muser.objects.filter(uName__exact=uName,uPassword__exact=uPassword,uType__exact=uType).values('uId')
#             if user:
#                 print(user[0]['uId'])
#                 if uType == "User":
#                     response =  render(request, 'MyTemp/Home/demo.html', {'userform': userform})
#                     response.set_cookie('uId', user[0]['uId'])
#                     response.set_cookie('uType', uType)
#                     return response
#                 if uType == "Apothecary":
#                     response = render(request, 'MyTemp/Home/Yishi.html', {'userform': userform})
#                     response.set_cookie('uId', user[0]['uId'])
#                     response.set_cookie('uType', uType)
#                     return response
#             else:
#                 return HttpResponse('Incorrect Password! Try Again!')
#     else:
#         userform = LoginUserForm()
#     return render(request,'MyTemp/Home/LoginPage.html',{'userform':userform})

def dologin(request):
    return render(request, 'MyTemp/Home/dologin.html')

def logout(request):
    return render(request,'MyTemp/Home/LoginPage.html',{'userform':userform})

def demo(request):
    return render(request, 'MyTemp/Home/demo.html')

def Yishi(request):
    return render(request, 'MyTemp/Home/Yishi.html')

from MyAdmin.models import TotalDrug
from MyAdmin.models import category
from django.core.paginator import Paginator
from django.db.models import Q
from MyWeb.models import Drug,Category

# def Shop(request):
#     return render(request, "Shop.html",)

def Shop_list(request, pIndex=1):
    # '''浏览信息'''
    # smod = Drug.objects
    # mywhere = {'search': '', 'type': ''}
    # # list = smod.filter(dStatus__lt=9)
    # list = smod.filter()
    # # 获取、判断并封装关keyword键搜索
    # kw = request.GET.get("search", None)
    # category = request.GET.get("category", None)
    # if kw:
    #     list = list.filter(Q(name__icontains=kw) | Q(id__exact=kw))
    #     mywhere['search'] = kw
    # if category:
    #     list = list.filter(type__exact=category)
    #     mywhere['type'] = category
    # # 执行分页处理
    # pIndex = int(pIndex)
    # page = Paginator(list, 28)  # 以8条每页创建分页对象
    # maxpages = page.num_pages  # 最大页数
    # # 判断页数是否越界
    # if pIndex > maxpages:
    #     pIndex = maxpages
    # if pIndex < 1:
    #     pIndex = 1
    # list2 = page.page(pIndex)  # 当前页数据
    # plist = page.page_range  # 页码数列表
    # # 封装信息加载模板输出
    # cmod = Category.objects
    # clist = cmod.filter(cStatus__lt=9)
    # context = {'categorylist': clist, "productlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages,
    #            'mywhere': mywhere}
    # return render(request, "Shop_list.html", context)
        '''浏览信息'''
        smod = TotalDrug.objects.all()
        mywhere = []
        # list = smod.filter(dStatus__lt=9)
        slist = smod
        context = {'druglist': slist}
        # 获取、判断并封装关keyword键搜索
        kw = request.GET.get("keyword", None)
        if kw:
            # 查询店铺名称中只要含有关键字就可以
            slist = slist.filter(Q(name__contains=kw))
            mywhere.append("keyword=" + kw)

        # # 获取、判断并封装菜品类别category_id搜索条件
        # id = request.GET.get('category_id', '')
        # if id != '':
        #     list = list.filter(category_id=id)
        #     mywhere.append("category_id=" + id)

        # 执行分页处理
        pIndex = int(pIndex)
        page = Paginator(slist, 15)  # 以15条每页创建分页对象
        maxpages = page.num_pages  # 最大页数
        # 判断页数是否越界
        if pIndex > maxpages:
            pIndex = maxpages
        if pIndex < 1:
            pIndex = 1
        list2 = page.page(pIndex)  # 当前页数据
        plist = page.page_range  # 页码数列表

        # 封装信息加载模板输出
        context = {"productlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
        return render(request, "Shop_list.html", context)

def Visualization(request):
    return render(request,"MyTemp/Shop/Visualization.html")