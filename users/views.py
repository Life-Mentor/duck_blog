from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, Reirster, ForgetPwdForm, ModifyPwdForm, forms 
from .models import EmailVerifyRecord, UserProfile
from utils.email_send import send_register_email

def active_user(request,active_code):
    all_records = EmailVerifyRecord.objects.filter(code = active_code)
    if all_records:
        for recod in all_records:
            email = recod.email
            user = User.objects.get(email=email)
            user.is_staff = True
            user.save()
    else:
        return HttpRequest('链接有误')
    return redirect('users:login')

class MyBlack(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get((Q(username=username)|Q(email=username)))
            if user.check_password(password):
                return user;
        except Exception as e:
            return None

class index(View):
    def get(self,request):
        return render(request,"index.html")

class login_view(View):
    def get(self,request):
        form = LoginForm()
        return render(request,"users/login.html",{'form':form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username  = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                responses = redirect(reverse('users:home'))
                responses.set_cookie("userid",user.id)
                return responses
            else:
                return HttpResponse("登录失败")
        return render(request,"users/login.html",{'form':form})

class reirster(View):
    def get(self,request):
        form = Reirster()
        return render(request,'users/reirster.html',{'form':form})
    def post(self,request):
        form = Reirster(request.POST)
        code = "OK"
        if form.is_valid():
            new_use = form.save(commit=False)
            new_use.set_password(form.cleaned_data.get('password'))
            new_use.email = form.cleaned_data.get('email')
            new_use.save()

            send_register_email(form.cleaned_data.get('email'),'register')
            return HttpResponse('注册成功')
        return render(request,'users/reirster.html',{'form':form,'code':code})

class forget_pwd(View):
    def get(self,request):
        form = ForgetPwdForm()
        return render(request,'users/forget_pwd.html',{'form':form})
    def post(self,request):
        form = ForgetPwdForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            exits = User.objects.filter(email=email).exists()
            if exits:
                send_register_email(email,'forget')
                return HttpResponse("发送成功请留意邮箱信息(垃圾信息)")
            else:
                return HttpResponse("邮箱未注册")
        return render(request,'users/forget_pwd.html',{'form':form})

class reset_pwd(View):
    def get(self,request,active_code):
        form = ModifyPwdForm()
        return render(request,'users/forget_pwd.html',{'form':form})
    def post(self,request,active_code):
        form = ModifyPwdForm(request.POST)
        if form.is_valid():
            record = EmailVerifyRecord.objects.get(code=active_code)
            email = record.email
            user = User.objects.get(email=email)
            user.email = email
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            code = '修改成功'
            return render(request,'users/reset_pwd.html',{'form':form,'code':code})
        else:
            code = '修改失败'
            return render(request,'users/reset_pwd.html',{'form':form,'code':code})

class user_home(View):
    def get(self,request):
        user = User.objects.get(username=request.user)
        return render(request,'users/home.html',{'user':user})






















