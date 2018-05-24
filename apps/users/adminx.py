# -*- coding: utf-8 -*-

import xadmin

from .models import EmailVerifyRecord, Banner


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





