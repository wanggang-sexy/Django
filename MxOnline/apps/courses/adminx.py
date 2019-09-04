# _*_ coding:utf-8 _*_
__auth__ = 'wanggang'
__date__ = '2019/1/8 0008 上午 11:52'

import xadmin


from .models import Course, Lesson, Video, CourseResource



class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']  # 搜索
    list_filter = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']  # 过滤


class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['course__name','name','add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']



class CourseResourceAdmin(object):
    list_display = ['course', 'name','download', 'add_time']
    search_fields = ['course', 'name','download']
    list_filter = ['course', 'name', 'download','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)