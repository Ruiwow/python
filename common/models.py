from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
# 客户名称
    name=models.CharField(max_length=200)
    # 联系电话
    phonenumber=models.CharField(max_length=200)
    # 地址
    address=models.CharField(max_length=200)


   

# 员工信息表
class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True,)
    # 员工姓名
    name=models.CharField(max_length=200)
    # 所属部门
    branch=models.CharField(max_length=200,null=True,blank=True)
    # 头像
    photo = models.ImageField(upload_to='photos')
    # 员工编号
    staff_number=models.CharField(max_length=200,null=True)
    # 是否管理员
    is_superuser = models.ImageField(max_length=200,null=True)
   

class Clocktime(models.Model):
    staff=models.ForeignKey(Staff,null=True,on_delete=models.PROTECT,blank=True)
    # 签到时间
    signin = models.DateTimeField(max_length=200,null=True)
    # 签退时间
    signout  = models.DateTimeField(max_length=200,null=True)
    # 工作时长
    worktimes=models.CharField(max_length=200,null=True,blank=True)
    # 日期（年月日）
    nowtime=models.CharField(max_length=200,null=True,blank=True)
     # 日期（年月）
    year_month=models.CharField(max_length=200,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,)
    # 状态码
    code=models.CharField(max_length=200,default='0')   

# 请假表
class leave(models.Model):

    staff=models.ForeignKey(Staff,on_delete=models.PROTECT,null=True,blank=True)
    # 请假原因
    unclockin_num=models.CharField(max_length=200)
    #时长
    leaveLength=models.CharField(max_length=200)
    #请假时间
    leavetime=models.DateTimeField(max_length=200)
    #是否批准，默认为0，待批，1不准，2准
    leavetime=models.DateTimeField(max_length=200,default='0')




    

from django.contrib import admin
admin.site.register(Customer)