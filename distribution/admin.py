from django.contrib import admin
import datetime

from django.contrib import admin, messages
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse

from simpleui.admin import AjaxAdmin
from distribution.models import FillMno
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


# Register your models here.
class ProxyResource(resources.ModelResource):
    class Meta:
        model = FillMno


@admin.register(FillMno)
class FillMnoAdmin(ImportExportActionModelAdmin, AjaxAdmin):
    resources_class = ProxyResource  # 定义数据库表

    # 需要展示的字段列表
    list_display = ('id', 'city', 'mno', 'mname', 'ct', 'mt')

    # 可以检索的字段
    search_fields = ('city', 'mno', 'mname')

    # 每页展示的行数
    list_per_page = 20

    # 设置每行的外键
    # raw_id_fields = ()

    # 需要筛选的列
    list_filter = ('ct',)

    # 点击字段，展示列表 跳转
    # list_display_links = ('mno',)

    # 跳转后的可编辑字段列表
    # list_editable = ('gender', 'age', 'phone', 'birthday', 'status', 'email')

    # 日期层次
    date_hierarchy = 'ct'

    # 点击添加时增加的字段
    fieldsets = ((None, {'fields': ('city', 'mno', 'mname')}),)

    # 保存后展示在最上方
    save_on_top = True

    # 是否显示选择的个数
    actions_selection_counter = True

    # 增加自定义按钮, 新增的标签都需要在这里定义
    # actions = ['make_copy', 'custom_button', 'layer_input']
