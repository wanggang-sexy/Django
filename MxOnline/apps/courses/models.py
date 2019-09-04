# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
from organization.models import CourseOrg
# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name=u"课程机构",null=True,blank=True)
    name = models.CharField(max_length=50,verbose_name=u"课程名")
    desc = models.CharField(max_length=300,verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(max_length=2,verbose_name=u"难度",choices=(("cj","初级"),("zj","中级"),("gj","高级")))
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长（分钟）")
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面图",max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    category = models.CharField(default=u"后端开发",max_length=30,verbose_name=u"课程类别")
    tag = models.CharField(default="",verbose_name=u"课程标签",max_length=20)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"点击数")


    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #获取课程章节数
        return self.lesson_set.all().count()
    def get_learn_users(self):
        #获取学习人数
        return self.usercourse_set.all()[:5]


    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加课程时间")


    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,verbose_name=u"章节")
    name = models.CharField(max_length=100,verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加视频时间")


    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"名称")
    download = models.FileField(upload_to="course/%Y/%m",verbose_name=u"资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加视频时间")


    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name




