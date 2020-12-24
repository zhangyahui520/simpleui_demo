from django.db import models

# Create your models here.

class DataIntegrityList(models.Model):
    # 定义字段
    database_name = models.CharField(max_length=50, verbose_name='数据库名')
    table_name = models.CharField(max_length=50, verbose_name='表名')
    note = models.CharField(max_length=100, verbose_name='备注')
    script_ct = models.DateField(verbose_name='脚本创建时间')
    regular_time = models.CharField(max_length=20, verbose_name='定时执行时间')
    monitoring_columns = models.CharField(max_length=100, verbose_name='监控字段')

    contains_choices = ((0, '不包含'), (1, '包含'))
    contains = models.IntegerField(choices=contains_choices, verbose_name='是否包含今天数据', default=1)

    root = models.CharField(max_length=11, verbose_name='根目录')
    path = models.CharField(max_length=11, verbose_name='脚本路径')

    flag_choices = ((0, '停止使用'), (1, '正在使用'))
    flag = models.IntegerField(choices=flag_choices, verbose_name='是否包含今天数据', default=1)

    ct = models.DateField(verbose_name='创建时间', auto_now_add=True)
    mt = models.DateField(verbose_name='更新时间', auto_now=True)

    # 相当于表名
    class Meta:
        verbose_name = '数据完整性监控'
        verbose_name_plural = '数据完整性监控管理'

    def __str__(self):
        return self.table_name