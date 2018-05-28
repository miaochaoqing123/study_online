from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 引用django 的Q对象方法:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    """用户激活功能"""
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')

        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        # 验证码
        register_form = RegisterForm()
        if register_form:
            return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        # 验证验证码是否正确
        if register_form.is_valid():
            # 开始注册
            user_name = request.POST.get('email', '')
            # 判断email是否存在
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已经存在'})
            pass_word = request.POST.get('password', '')

            # 实例化user
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()

            # 第2个参数register ,是model 定义好的send_type类型
            send_register_email(user_name, 'register')
            return render(request, 'login.html')
        else:
            render(request, 'register.html', {'register_form': register_form})

        return render(request, 'register.html',  {'register_form': register_form})


class LoginView(View):
    """
    用户登录
    引用类的方法:
    1. 继承 from django.views.generic.base import View
    2. 重写get 和post
    3. 还在在urls更改LoginView.as_view()
    """
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 用 is_valid 方法判断前端的数据是否有错
            # 验证成功则正常跳转
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            # 还要改判断用户是否存在
            email = request.POST.get('email', '')
            if not UserProfile.objects.filter(email=email):
                return render(request, 'forgetpwd.html', {'msg': '用户不存在'})

            # 第2个参数forget ,是model 定义好的send_type类型
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')

        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    """用户重置密码页面"""
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')

        return render(request, 'forgetpwd.html')


class ModifyPwdView(View):
    """用户重置密码功能"""
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email' '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg': '两次密码不一至'})

            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'modify_form': modify_form, 'email': email})





# def user_login(request):
#     # 用户名密码登录功能
#     if request.method == 'POST':
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'msg': '用户名或密码错误'})
#     elif request.method == 'GET':
#         return render(request, 'login.html', {})








