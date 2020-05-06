from django.http import JsonResponse
import json
from common.models import Customer,Clocktime,Staff,User
from django.utils import timezone
import os
from datetime import datetime
import time
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings



def fun():
    os.system("python  mgr/人脸识别.py")




def dispatcher(request):
    # 浏览器关闭时清除cookie   
    request.session.set_expiry(0)
   
    if 'usertype' not in request.session:    
       
        return JsonResponse({
            'ret': 302,
            'msg': '管理员',
             'redirect': '/mgr/login.html'
        }, 
            )
      

       

        


    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)
     

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'validatelogon':
        return validatelogon(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)
    elif action == 'face_customer':
        return facecustomer(request)
    elif action == 'signin_customer':
        return signincustomer(request)
    elif action == 'logout_customer':
        return logoutcustomer(request)
    elif action == 'list_staff':
        return liststaff(request)
    elif action == 'export':
        return export(request)
    elif action == 'vip':
        return vip(request)
    elif action == 'Remarks':
        return Remarks(request)
    elif action == 'Clocktime_list':
        return Clocktime_list(request)
    

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})



# 导出员工信息

def export(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Staff.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)
   
    return JsonResponse({'code': 0, 'data': retlist,})

# 获取员工信息列表并分页
def liststaff(request):
    name = request.GET.get('name')
    if name is None:
        qs = Staff.objects.filter(name__contains='').values()
        retlist = list(qs)
        
        a = len(retlist)
  
        paginator = Paginator(retlist, 10)

        if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page = request.GET.get('page')
       
            try:
                List = list(paginator.page(page))
            
        # todo: 注意捕获异常
            except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
                books = paginator.page(1)
            except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                books = paginator.page(paginator.num_pages)

        return JsonResponse({'code': 0,'data':List,'count':a})
   
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    else:
        qs = Staff.objects.filter(name__contains=name).values()

    # # 将 QuerySet 对象 转化为 list 类型
    # # 否则不能 被 转化为 JSON 字符串
        retlist = list(qs)
    
        a = len(retlist)
  
        paginator = Paginator(retlist, 10)

        if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page = request.GET.get('page')
       
            try:
                List = list(paginator.page(page))
            
        # todo: 注意捕获异常
            except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
                books = paginator.page(1)
            except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                books = paginator.page(paginator.num_pages)

        return JsonResponse({'code': 0,'data':List,'count':a})



def validatelogon(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    staff_id = request.params['id']
    year_month = request.params['year_month']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        time = Clocktime.objects.filter(code = '0',staff_id = staff_id,year_month=year_month)      
    except Clocktime.DoesNotExist:    
        return JsonResponse({'ret': "meiyou"})
    

    a = time.count()
    
    print(a)
    

  
    return JsonResponse({'ret': 12345,'count' : a})
    

  

def addcustomer(request):
  
   
    name    = request.params['name']
    img = request.params['img']

    
    # image = request.FILES.get('file',None)
    
    # path=default_storage.save('img/'+image.name,ContentFile(image.read()))

    # tmp_file = os.path.join(settings.MEDIA_ROOT,path)
    print(img)
    # # 从请求消息中 获取要添加客户的信息
    # # 并且插入到数据库中
    # # 返回值 就是对应插入记录的对象 
    record = Staff.objects.create(name=name,photo=img
                           )


    return JsonResponse({'ret': 0, 'id':record.id})



def modifycustomer(request):

    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    
    customerid = request.params['id']
    newdata    = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return  JsonResponse({
                'ret': 1,
                'msg': f'id 为`{customerid}`的客户不存在'
        })


    if 'name' in  newdata:
        customer.name = newdata['name']
    if 'phonenumber' in  newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in  newdata:
        customer.address = newdata['address']

    # 注意，一定要执行save才能将修改信息保存到数据库
    customer.save()

    return JsonResponse({'ret': 0})

def deletecustomer(request):

    staff_id = request.params['id']
    
  
    try:
        # 根据 id 从数据库中找到相应的客户记录
        
        staff = Staff.objects.get(id=staff_id)
        clocktime = Clocktime.objects.filter(staff_id=staff_id)
        user=User.objects.get(id=staff_id)
        
    except staff.DoesNotExist:
        return JsonResponse({
                'ret': 1,
                'msg': f'id 为`{staff_id}`的客户不存在'
        })

    # delete 方法就将该记录从数据库中删除了
    
    staff.delete()
    clocktime.delete()
    user.delete()



    qs = Staff.objects.filter(name__contains='').values()
    retlist = list(qs)
    
    a = len(retlist)
   
   

    return JsonResponse({'ret': 0,'count':a})


# 打卡
def facecustomer(request):

    staff_id = request.params['id']
    name = request.params['name']
    Nowtime = request.params['Nowtime']
    year_month = request.params['year_month']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        time = Clocktime.objects.get(staff_id=staff_id,nowtime=Nowtime)
       
    except Clocktime.DoesNotExist:

        fun()
        record = Clocktime.objects.create(staff_id=staff_id,nowtime=Nowtime,name=name)
        record.signin = datetime.now()
        record.year_month = year_month
        record.save()
        return JsonResponse({'ret': '打卡呈贡'})
    

    
   
    


    return JsonResponse({'ret': '已经打过卡啦'})

# 签退
def logoutcustomer(request):

    staff_id = request.params['id']
    Nowtime = request.params['Nowtime']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        tim = Clocktime.objects.get(staff_id=staff_id,nowtime=Nowtime)
       
    except Clocktime.DoesNotExist:
        return  JsonResponse({
                'ret': 1,
                'msg': '您今日未打卡'
        })
  
    tim.signout = datetime.now()
    

    a=tim.signin
    b=tim.signout
    starttime = datetime.strptime(a.strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')#必须将时间先格式化
 
    endtime = datetime.strptime(b.strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
 
    worktimes= round(((endtime-starttime).seconds)/3600)  #起始时间减去结束时间
    
    
    tim.worktimes = worktimes
    tim.save()

    return JsonResponse({'ret': 0})

    

def signincustomer(request):

    timeid = request.params['id']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        tim = Clocktime.objects.get(id=timeid)
       
    except Clocktime.DoesNotExist:
        return  JsonResponse({
                'ret': 1,
                'msg': f'id 为`{timeid}`的客户不存在'
        })
    
   
    tim.signin = datetime.now()


    tim.save()

    return JsonResponse({'ret': 0})


def vip(request):

    id = request.params['id']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        user= User.objects.get(id=id)
       
    except User.DoesNotExist:
        return  JsonResponse({
                'ret': 1,
                'msg': f'id 为`{id}`的客户不存在'
        })
    
    user.is_superuser ='1'
    


    user.save()

    return JsonResponse({'ret': 0})



def Remarks(request):

    
    staff_id = request.params['id']
    # Nowtime = request.params['Nowtime']
    year_month = request.params['year_month']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        clocktime= Clocktime.objects.filter(staff_id=staff_id,year_month=year_month).values()

    except Clocktime.DoesNotExist:
        return  JsonResponse({
                'ret': 1,
                'msg': f'id 为`{id}`的客户不存在'
        })
    retlist = list(clocktime)
    print(retlist)

    return JsonResponse({'ret': 0,'data':retlist})


def Clocktime_list(request):

    qs = Clocktime.objects.values()
    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)
    a = len(retlist)
  
    paginator = Paginator(retlist, 10)
    
   
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page = request.GET.get('page')
       
            try:
                List = list(paginator.page(page))
            
        # todo: 注意捕获异常
            except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
                books = paginator.page(1)
            except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                books = paginator.page(paginator.num_pages)

    return JsonResponse({'code': 0,'data':List,'count':a})

