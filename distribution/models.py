from django.db import models


# Create your models here.

class FillMno(models.Model):
    # 定义字段
    city = models.CharField(max_length=10, verbose_name='城市名')
    mno = models.CharField(max_length=128, verbose_name='机器编号', help_text='请输出正确的机器编号', unique=True)
    mname = models.CharField(max_length=128, verbose_name='机器名称')
    ct = models.DateField(verbose_name='创建时间', auto_now_add=True)
    mt = models.DateField(verbose_name='更新时间', auto_now=True)

    # 相当于表名
    class Meta:
        verbose_name = '补满机器'
        verbose_name_plural = '补满机器管理'

    def __str__(self):
        return self.mno


class WhiteListOfWithdrawn(models.Model):
    # 定义字段
    city = models.CharField(max_length=10, verbose_name='城市名')
    aid = models.CharField(max_length=10, verbose_name='商品编号', help_text='请输出正确的商品编号')
    gcid = models.CharField(max_length=30, verbose_name='GCID')
    aname = models.CharField(max_length=100, verbose_name='商品名称')
    note = models.CharField(max_length=100, verbose_name='备注')
    ct = models.DateField(verbose_name='创建时间', auto_now_add=True)
    mt = models.DateField(verbose_name='更新时间', auto_now=True)

    # 相当于表名
    class Meta:
        verbose_name = '撤货白名单'
        verbose_name_plural = '撤货白名单管理'

    def __str__(self):
        return self.aid

class VehicleInformation(models.Model):
    # 定义字段
    city = models.CharField(max_length=10, verbose_name='城市名')
    name = models.CharField(max_length=20, verbose_name='姓名')
    car_info = models.CharField(max_length=100, verbose_name='车辆信息')
    quantity_available = models.IntegerField(verbose_name='载货量')
    can_withdrawn = models.IntegerField(verbose_name='可撤货量')
    ct = models.DateField(verbose_name='创建时间', auto_now_add=True)
    mt = models.DateField(verbose_name='更新时间', auto_now=True)

    # 相当于表名
    class Meta:
        verbose_name = '车辆信息'
        verbose_name_plural = '车辆信息管理'

    def __str__(self):
        return self.name



class CityMasterPhone(models.Model):
    # 定义字段
    city = models.CharField(max_length=10, verbose_name='城市名')
    name = models.CharField(max_length=20, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    ct = models.DateField(verbose_name='创建时间', auto_now_add=True)
    mt = models.DateField(verbose_name='更新时间', auto_now=True)

    # 相当于表名
    class Meta:
        verbose_name = '城市负责人联系电话'
        verbose_name_plural = '城市负责人联系方式管理'

    def __str__(self):
        return self.city