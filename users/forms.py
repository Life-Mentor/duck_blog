from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32,widget=forms.TextInput(attrs={ 'class': 'input is-success', 'placeholder':"Primary input",'style':"width:220px;"}))
    password = forms.CharField(label='密码',max_length=32,widget=forms.PasswordInput(attrs={'class':'input is-success','placeholder':'Primary input','style':"width:220px;"}))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username == password:
            raise forms.ValidationError('用户名与密码不能相同')
        return password

class Reirster(forms.ModelForm):
    email = forms.EmailField(label='邮箱', max_length=32, widget=forms.EmailInput(attrs={ 'class': 'input', 'placeholder': '用户名/邮箱' }))
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(attrs={ 'class': 'input', 'placeholder': '密码'}))
    # password1 = forms.CharField(label='再次输入密码', min_length=6, widget=forms.PasswordInput(attrs={ 'class': 'input', 'placeholder': '再次输入密码'}))
    class Meta:
        model = User
        fields = ('username','password')

    def clean_email(self):
        """ 验证用户是否存在 """
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('此邮箱已被注册!')
        return email
    def clean_user(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            raise forms.ValidationError('用户名已存在')
        return username
    def clean_pwd(self):
        print(self)
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("两次密码不一样")
        return self.cleaned_data['password1']

class ForgetPwdForm(forms.Form):
    email = forms.EmailField(label='请输入注册时的邮箱地址',min_length=4,widget=forms.EmailInput(attrs={'class':'inpur','placeholder':'用户名/邮箱'}))

class ModifyPwdForm(forms.Form):
    """修改密码表单"""
    password = forms.CharField(label="输入新密码", min_length=6, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '输入密码'}))









