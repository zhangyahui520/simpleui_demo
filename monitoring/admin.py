from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportActionModelAdmin
from simpleui.admin import AjaxAdmin

from monitoring.models import DataIntegrityList


@admin.register(DataIntegrityList)
class DataIntegrityListAdmin(ImportExportActionModelAdmin, AjaxAdmin):
    # resources_class = ProxyResource  # 定义数据库表

    # 需要展示的字段列表
    list_display = ('id', 'database_name', 'table_name', 'note', 'script_ct', 'regular_time', 'monitoring_columns',
                    'contains', 'root', 'path', 'flag', 'ct', 'mt')

    # 可以检索的字段
    search_fields = ('database_name', 'table_name', 'note')

    # 每页展示的行数
    list_per_page = 20

    # 需要筛选的列
    list_filter = ('ct',)

    # 日期层次
    date_hierarchy = 'ct'

    # 点击添加时增加的字段
    fieldsets = (
    (None, {'fields': ('database_name', 'table_name', 'note', 'script_ct', 'regular_time', 'monitoring_columns',
                       'contains', 'root', 'path', 'flag',)}),)

    # 保存后展示在最上方
    save_on_top = True

    # 是否显示选择的个数
    actions_selection_counter = True
