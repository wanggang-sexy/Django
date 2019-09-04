# _*_ coding:utf-8 _*_
#@__auth__ = 'wanggang'
#@__date__ = 2019/4/17 0017 上午 11:51
#@__Software = PyCharm
from django.urls import path,re_path,include
from django.views.generic import TemplateView

from .views import CourseListView,CourseDetailView





urlpatterns = [

    #课程相关列表页
    re_path(r'^list/$',CourseListView.as_view(),name="course_list"),

    #课程详情页
    re_path(r'^detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(),name="course_detail")


    ]
