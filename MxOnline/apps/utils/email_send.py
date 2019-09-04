# _*_ coding:utf-8 _*_
__auth__ = 'wanggang'
__date__ = '2019/1/21 0021 上午 11:19'


from random import Random
from users.models import EmailVerifyRecord


from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars)
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str

def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    #发送邮件代码
    email_title = ''#邮件标题
    email_body = ''#邮件内容

    if send_type == 'register':
        email_title = "慕学网注册账号激活"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            print("邮件发送成功")
    elif send_type == 'forget':
        email_title = "慕学网注册账号密码重置链接"
        email_body = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print("邮件发送成功")

