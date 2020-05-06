from django.urls import path
from . import views
from sales.views import listorders,listcustomers
# 设置路由入口
urlpatterns = [
   
    path('orders/', listorders),
    path('customers/', listcustomers),
]
 