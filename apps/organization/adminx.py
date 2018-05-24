# -*- coding: utf-8 -*-

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    # 在后台显示的字段名
    list_display = ['name', 'desc', 'add_time']
    # xadmin 后台的搜索字段
    search_fields = ['name', 'desc']
    # 过滤器
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    # 在后台显示的字段名
    list_display = ['name', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    # xadmin 后台的搜索字段
    search_fields = ['name', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    # 过滤器
    list_filter = ['name', 'click_nums', 'fav_nums','image', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    # 在后台显示的字段名
    list_display = ['org', 'name', 'work_yeas', 'work_company', 'points', 'click_nums', 'fav_nums', 'add_time']
    # xadmin 后台的搜索字段
    search_fields = ['org', 'name', 'work_yeas', 'work_company', 'points', 'click_nums', 'fav_nums']
    # 过滤器
    list_filter = ['org', 'name', 'work_yeas', 'work_company', 'points', 'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)