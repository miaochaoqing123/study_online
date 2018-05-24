# -*- coding: utf-8 -*-

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    """后台添加主题选项"""
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    """修改后台左上角和底部信息"""
    site_title = '缪氏后台管理系统'  # 左上角和title
    site_footer = '缪氏教育在线网'  # 底部
    menu_style = 'accordion'  # 左边列表的伸缩


class EmailVerifyRecordAdmin(object):
    # 在后台显示的字段名
    list_display = ['code', 'email', 'send_type', 'send_time']
    # xadmin 后台的搜索字段
    search_fields = ['code', 'email', 'send_type']
    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # 在后台显示的字段名
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # xadmin 后台的搜索字段
    search_fields = ['title', 'image', 'url', 'index']
    # 过滤器
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# 注册主题
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 修改后台左上角和底部信息
xadmin.site.register(views.CommAdminView, GlobalSetting)




