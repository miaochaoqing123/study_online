# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # username 和 password 必须与login.html 里的 name 一致
    username = forms.CharField(required=True)  # required=True 表示不能为空
    password = forms.CharField(required=True, min_length=6, max_length=20)


class RegisterForm(forms.Form):
    """注册页面的验证码 """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ForgetForm(forms.Form):
    """忘记页面的验证码 """
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ModifyPwdForm(forms.Form):
    """重置密码"""
    password1 = forms.CharField(required=True, min_length=6, max_length=20)
    password2 = forms.CharField(required=True, min_length=6, max_length=20)






