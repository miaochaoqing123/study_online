# -*- coding: utf-8 -*-
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def random_str(randomlength=8):
    str_s = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str_s += chars[random.randint(0, length)]
    return str_s


# 邮箱验证send_type='register'为注册
def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '缪氏教育在线网注册激活链接'
        # email_body = '请点击下面的链接激活您的账号: <a href="http://127.0.0.1:8000/active/%s">点击连接</a>' % code
        email_body = '请点击下面的链接激活您的账号: http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM,[email])

        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '缪氏教育在线网重置密码链接'
        email_body = '请点击下面的链接重置您的密码: http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status:
            pass
















