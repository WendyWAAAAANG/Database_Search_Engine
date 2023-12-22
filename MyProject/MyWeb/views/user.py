from django.db import connection

def searchDrug(requeat,):
    mod = Drug.objects
    Druglist = mod.filter(drugid=drugid).values()
    Druglist = list(Druglist)
    return JsonResponse({"data": Druglist})


def getAll(request):
    mod = Drug.objects # 获取Drug模型的Model操作对象
    Druglist = mod.all().values()  #获取所有数据
    Druglist = list(Druglist) #转化为列表属性
    pagenum = request.GET.get('pagenum')
    p = Paginator(Druglist, pagenum) #返回分页对象，参数为列表数据，每面数据的条数
    page = request.GET.get('page') #获取当前页页数
    if page == '':
        page = '1'
    page = int(page)
    pages = p.num_pages
    total = p.count
    pageInfo = p.page(page)  # 下标以1开始，如果提供的页码不存在，抛出InvalidPage异常
    hasPrevious = pageInfo.has_previous() #如果有上一页返回True
    hasnext = pageInfo.has_next() #如果有下一页返回True
    plist = list(p.page_range) # 页码列表，从1开始，例如[1, 2, 3, 4]
    number = pageInfo.number # 当前页码
    object_list = pageInfo.object_list #当前页上所有对象的列表
    print(pages,total,hasPrevious,hasnext,number,plist)
    return JsonResponse({'data': object_list,'pages':pages,'total':total,'hasPrevious':hasPrevious,'hasnext':hasnext,'number':number,'plist':plist})