from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from django.urls import reverse


class Wuliu(models.Model):
    # max_length：字段最大长度， verbose_name： 表示别名， help_text：提示字段， unique：进行查重，值是唯一的， db_index：数据库的字段自增，
    # null:输入值为null， blank：允许为空, validators:提示输入区间, auto_now：如果不填入，则自动填充当前时间

    # 需要字段
    # 员工名称
    name = models.CharField(max_length=128, verbose_name='员工名称', help_text='员工名称不能重复', null=False, blank=False,
                            db_index=True)

    # 性别
    gender_choices = ((0, '未知'), (1, '男'), (2, '女'))
    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)

    # 年龄
    age = models.IntegerField(verbose_name='年龄', validators=[MinValueValidator(1), MaxValueValidator(100)])

    # 手机号
    phone = models.CharField(max_length=11, verbose_name='手机号')

    # 身份证号
    idCard = models.CharField(max_length=18, verbose_name='身份证号', help_text='请输出18位的身份证号码', null=True, blank=True)

    # 出生日期
    birthday = models.DateField(verbose_name='出生日期')

    # 负责城市, 通过级联产生

    # 职务， 关联其他类，以外键的形式

    # 状态
    status_choices = ((0, '在职'), (1, '请假'), (2, '离职'))
    status = models.IntegerField(choices=status_choices, verbose_name='状态', default=0)

    # 邮箱地址
    email = models.EmailField(verbose_name='邮箱地址')

    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    # 更新时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '物流'
        verbose_name_plural = '物流人员管理'

    def __str__(self):
        return self.name
