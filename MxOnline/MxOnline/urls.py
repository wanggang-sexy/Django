# _*_ coding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT
import xadmin


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',TemplateView.as_view(template_name="index.html"),name="index"),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    re_path(r'captcha/',include('captcha.urls')),
    re_path(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),
    path('forget/',ForgetPwdView.as_view(),name="forget_pwd"),
    re_path(r'^reset/(?P<active_code>.*)/$',ResetView.as_view(),name="reset_pwd"),
    path('modify_pwd/',ModifyPwdView.as_view(),name="modify_pwd"),

    #课程机构url配置
    path('org/',include(('organization.urls','organization'), namespace="org")),

    #课程相关url配置
    path('course/',include(('courses.urls','courses'), namespace="course")),




    #配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

]
