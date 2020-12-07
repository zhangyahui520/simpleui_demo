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
