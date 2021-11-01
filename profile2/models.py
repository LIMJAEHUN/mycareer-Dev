from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profile2(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 현 계정의 사용자를 가져올 수 있음.
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    nickname = models.CharField(max_length=64,verbose_name='닉네임')
    phone_number = models.CharField(max_length=12,verbose_name='전화번호')
    university = models.CharField(max_length=32,verbose_name='대학교',null=True)
    profile_photo = models.ImageField(blank=True,verbose_name='프로필사진')                 # 값을 채워넣지 않아도 되는 속성.
    id = models.AutoField(primary_key=True,null=False)