# _*_ coding:utf-8 _*_
__auth__ = 'wanggang'
__date__ = '2019/1/8 0008 上午 11:11'

import xadmin

from .models import EmailVerifyRecord
from .models import Banner

class EmailVerifyRecordAdmin(object):
    list_display = ['code','emol','send_type','send_time']#显示
    search_fields = ['code','emol','send_type'] #搜索
    list_filter = ['code','emol','send_type','send_time'] #过滤

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']#显示
    search_fields = ['title', 'image', 'url', 'index']  # 搜索
    list_filter = ['title', 'image', 'url', 'index','add_time']  # 过滤

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
