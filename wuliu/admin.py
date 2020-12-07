from django.contrib import admin
import datetime

from django.contrib import admin, messages
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse

from simpleui.admin import AjaxAdmin
from wuliu.models import Wuliu
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


# Register your models here.
class ProxyResource(resources.ModelResource):
    class Meta:
        model = Wuliu


@admin.register(Wuliu)
class WuliuAdmin(ImportExportActionModelAdmin, AjaxAdmin):
    resources_class = ProxyResource  # 定义数据库表

    # 需要展示的字段列表
    list_display = (
        'id', 'name', 'gender', 'age', 'phone', 'idCard', 'birthday', 'status', 'email', 'create_time', 'update_time')

    # 需要检索的字段
    search_fields = ('name', 'idCard', 'email')

    # 每页展示的行数
    list_per_page = 20

    # 设置每行的外键
    # raw_id_fields = ()

    # 需要筛选的列
    list_filter = ('create_time',)

    # 点击字段，展示列表 跳转
    list_display_links = ('name',)

    # 跳转后的可编辑字段列表
    list_editable = ('gender', 'age', 'phone', 'birthday', 'status', 'email')

    # 日期层次
    date_hierarchy = 'create_time'

    # 点击添加时增加的字段
    fieldsets = ((None, {'fields': ('name', 'gender', 'age', 'phone', 'idCard')}),
                 ('other_info', {'classes': ('collapse', 'wide', 'extrapretty'),
                                 'fields': ('birthday', 'status', 'email'), }))

    # 保存后展示在最上方
    save_on_top = True

    # 是否显示选择的个数
    actions_selection_counter = True

    # 测试是否正确
    @transaction.atomic
    def test(self, request, queryset):
        messages.add_message(request, messages.SUCCESS, '未检测到数据')
        pass

    # 自 3.4+ 支持confirm确认提示
    test.confirm = '您确定要点击测试按钮吗？'

    # 增加自定义按钮, 新增的标签都需要在这里定义
    actions = [test, 'make_copy', 'custom_button', 'layer_input']

    # 弹出框输入
    def layer_input(self, request, queryset):
        # 这里的queryset，会有数据过滤，只包含选中的数据

        post = request.POST
        # 这里获取到数据后，可以做些业务处理

        # post中的_action 是方法名
        # post中的 _selected是选中的数据，逗号分割
        # if not post.get('_selected'):
        #     return JsonResponse(data={
        #         'status': 'error',
        #         'msg': '请先选中数据！'
        #     })
        # else:
        # 返回处理结果
        return JsonResponse(data={
            'status': 'success',
            'msg': '处理成功！'
        })

    # 定义按钮的属性
    layer_input.short_description = '弹出对话框输入'  # 按钮描述
    layer_input.type = 'success'  # 按钮类型
    layer_input.icon = 'el-icon-s-promotion'  # 按钮的图标

    # 指定一个输入参数， 应该是一个数组

    # 指定为弹出层， 这个参数是关键
    layer_input.layer = {

        # 弹出框中的输出入配置
        'title': '弹出框输入框',  # 对话框标题
        'tips': '这个弹出对话框需要在admin中进行定义, 数据新增编辑等功能，需要自己实现。',  # 提示信息
        'confirm_button': '确认提交',  # 确认按钮显示字段
        'cancel_button': '取消',  # 取消按钮显示字段

        # 弹出框的外形设置
        'width': '40%',

        # 表单追踪lable的宽度， 对应element-UI的lable-width，默认为80px
        'labelWidth': '80px',

        # 表单字段
        'params': [{
            # 这里的type 对应el-input的原生input属性，默认为input
            'type': 'input',
            # key 对应post参数中的key
            'key': 'name',
            # 显示的文本
            'label': '名称',
            # 为空校验，默认为False
            'require': True
        }, {
            'type': 'select',
            'key': 'gender',
            'label': '性别',
            'width': '80px',
            # size对应elementui的size，取值为：medium / small / mini
            'size': 'small',
            # value字段可以指定默认值
            'value': '1',
            'options': [{
                'key': '0',
                'label': '未知'
            }, {
                'key': '1',
                'label': '男'
            }, {
                'key': '2',
                'label': '女'
            }]

        }, {
            'type': 'input_number',
            'key': 'age',
            'label': '年龄',
            'size': 'medium',
            'value': '20'
        }, {
            'type': 'input',
            'key': 'phone',
            'label': '手机号',
            'size': 'mini'
        }, {
            'type': 'input',
            'key': 'idCard',
            'label': '身份证号',
            'width': '120px'
        }, {
            'type': 'date',
            'key': 'birthdate',
            'label': '出生日期'
        }, {
            'type': 'select',
            'key': 'status',
            'label': '状态',
            'width': '80px',
            # size对应elementui的size，取值为：medium / small / mini
            'size': 'small',
            # value字段可以指定默认值
            'value': '0',
            'options': [{
                'key': '0',
                'label': '在职'
            }, {
                'key': '1',
                'label': '请假'
            }, {
                'key': '2',
                'label': '离职'
            }]
        }, {
            'type': 'input',
            'key': 'email',
            'label': '邮箱地址'
        }]
    }

    # 跳转按钮
    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '跳转'

    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'el-icon-share'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'primary'

    # 给按钮字体追加自定义的颜色
    custom_button.style = 'color:black;'

    # 链接按钮，设置之后直接访问该链接
    # 3种打开方式
    # action_type： 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 注意： 设置了action_type，不设置url，页面内将报错

    custom_button.action_type = 1
    custom_button.action_url = 'http://0.0.0.0:8080/admin/'

    # 复制按钮
    def make_copy(self, request, queryset):
        # 获取post传递的字段
        ids = request.POST.getlist('_selected_action')
        print(ids)
        print(Wuliu.objects)
        # 逻辑处理
        for id in ids:
            print(Wuliu.objects.get(id=id))
            wuliu = Wuliu.objects.get(id=id)  # 从指定对象中回去获取指定值

            # 创建一个对象实例
            Wuliu.objects.create(name=wuliu.name,
                                 gender=wuliu.gender,
                                 age=wuliu.age,
                                 idCard=wuliu.idCard,
                                 phone=wuliu.phone,
                                 birthday=wuliu.birthday,
                                 email=wuliu.email)

        # 定义返回信息
        messages.add_message(request, messages.SUCCESS, '复制成功，复制了{}个员工。'.format(len(ids)))

    # 定义标签信息
    make_copy.short_description = '复制'
    make_copy.icon = 'el-icon-document-copy'
    make_copy.type = 'info'

# admin.site.register(Wuliu, WuliuAdmin)
