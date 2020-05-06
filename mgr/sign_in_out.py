from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout


# 登录处理
def signin( request):

    request.params = json.loads(request.body)
    info=request.params['data']
    userName= info['username']
    passWord= info['password']
   
    # 从 HTTP POST 请求中获取用户名、密码参数
    # userName = request.POST.get('username')
    # passWord = request.POST.get('password')

    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)
    # user = Staff.objects.filter(username = userName)
    # print(user)
    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'
              
                return JsonResponse({'ret': 0,})
                
            else:
                request.session['usertype'] = 'staff'
                return JsonResponse({'ret': 1, 'username':user.username,'id':user.id,'msg': '员工登录'})
        else:
            return JsonResponse({'ret': 2, 'msg': '用户已经被禁用'})
        
    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 3, 'msg': '用户名或者密码错误'})


# 登出处理
def signout( request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})
