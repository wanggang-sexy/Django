# _*_ coding:utf-8 _*_
__auth__ = 'wanggang'
__date__ = '2019/1/8 0008 下午 2:30'

import xadmin
from xadmin import views
from .models import CityDict,CourseOrg,Teacher


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = u"慕学后台管理系统"
    site_footer = u"慕学在线网"
    menu_style = "accordion"

class CityDictAdmin(object):
    list_display = ['name', 'desc','add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc','add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city','add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums','image','address','city','add_time']


class TeacherAdmin(object):
    list_display = ['org','name', 'work_years', 'work_company', 'work_position','points','click_nums','fav_nums','add_time']
    search_fields = ['org','name', 'work_years', 'work_company', 'work_position','points','click_nums','fav_nums']
    list_filter = ['org','name', 'work_years', 'work_company', 'work_position','points','click_nums','fav_nums','add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)




