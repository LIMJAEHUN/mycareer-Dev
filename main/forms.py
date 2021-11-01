from django import forms
from .models import mainconsult
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from .models import Profile
from main import models



class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    #university = forms.

    class Meta:
        model = User
        fields = ("username","password1","password2", "email")


class consult_form(forms.Form):
    username= forms.CharField(label='회원아이디')
    name = forms.CharField(label='이름' ,max_length=10, initial='')
    phone_number = forms.CharField(label='전화번호',max_length=14, widget=forms.TextInput(attrs={'placeholder':'-와 띄어쓰기를 제외하고 입력하세요.'}))
    university = forms.CharField(label='대학교')
    #contents = forms.CharField(label='상담내용', max_length=500, widget=forms.Textarea(attrs={'row':5,'placeholder':'500자 이내로 작성해주세요.'}))
    contents = forms.CharField(label='상담내용', max_length=300)
    # class Meta:
    #     model = mainconsult
    #     fields = ("name","phone_number","university", "postname","contents")


class CustomUserChangeForm(UserChangeForm):
    password = None
    # UserChangeForm에서는 password를 수정할 수 없다.
    # 하지만 이렇게 None 값으로 지정해주지 않으면 password를 변경할 수 없다는 설명이 화면에 표현된다.
    class Meta:
        #model = get_user_model()
        model = User
        fields = ['email', 'first_name', 'last_name',]

class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(label="닉네임", required=False)
    university = forms.CharField(label="대학교", required=False)
    phone_number = forms.CharField(label="전화번호",max_length=14, required=False)
    profile_photo = forms.ImageField(label="프로필사진", required=False)

    class Meta:
        model = Profile
        fields = ['nickname', 'phone_number', 'profile_photo', 'university']

