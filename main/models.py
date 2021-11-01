from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.safestring import mark_safe
# class bookmark(models.Model):
#     postname = models.CharField(max_length=50)


class MainPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    rogophoto = models.ImageField(blank=True, null=True, verbose_name='회사사진')
    postname = models.CharField(max_length=50,verbose_name='회사명')
    area = models.CharField(max_length=10, blank=True, null=True, verbose_name='근무지')
    author = models.CharField( max_length=16, blank=True, null=False, verbose_name='작성자')
    job = models.CharField(max_length=10, blank=True, null=True,verbose_name='직무')
    etc = models.CharField(max_length=30, blank=True, null=True,verbose_name='우대사항' )
    ck = RichTextUploadingField(blank=True,null=True,verbose_name='본문내용')
    point_id = models.IntegerField(verbose_name='회사번호')
    #ck = RichTextUploadingField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'main_post'

class chosunPost(models.Model):
    id = models.OneToOneField("MainPost",on_delete=models.CASCADE, db_column="id",primary_key=True)
    rogophoto = models.ImageField(blank=True, null=True, verbose_name='회사사진')
    postname = models.CharField(max_length=50,verbose_name='회사명')
    area = models.CharField(max_length=10, blank=True, null=True, verbose_name='근무지')
    author = models.CharField(max_length=16, blank=True, null=False, verbose_name='작성자')
    job = models.CharField(max_length=10, blank=True, null=True,verbose_name='직무')
    etc = models.CharField(max_length=30, blank=True, null=True,verbose_name='우대사항' )
<<<<<<< HEAD
    ck = RichTextUploadingField(blank=True, null=True)
=======
    ck = RichTextUploadingField(blank=True, null=True,verbose_name='본문내용')
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    point_id = models.IntegerField(verbose_name='회사번호',default=1)


    class Meta:
        managed = False
        db_table = 'chosunPost'



class member(models.Model):
    id = models.CharField(db_column='University', max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=8)
    author = models.CharField(max_length=16)
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'member'

    def __str__(self):
        return self.name



class seoulPost(models.Model):
    id = models.OneToOneField("MainPost",on_delete=models.CASCADE, db_column="id",primary_key=True)
    rogophoto = models.ImageField(blank=True, null=True, verbose_name='회사사진')
    postname = models.CharField(max_length=50,verbose_name='회사명')
    area = models.CharField(max_length=10, blank=True, null=True, verbose_name='근무지')
    author = models.CharField(max_length=16, blank=True, null=False, verbose_name='작성자')
    job = models.CharField(max_length=10, blank=True, null=True,verbose_name='직무')
    etc = models.CharField(max_length=30, blank=True, null=True,verbose_name='우대사항' )
<<<<<<< HEAD
    ck = RichTextUploadingField(blank=True, null=True)
=======
    ck = RichTextUploadingField(blank=True, null=True,verbose_name='본문내용')
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    point_id = models.IntegerField(verbose_name='회사번호',default=2)


    class Meta:
        managed = False
        db_table = 'seoulPost'


class chosunconsult(models.Model):
    id = models.AutoField(primary_key=True)
<<<<<<< HEAD
    name = models.CharField(max_length=30, verbose_name='이름')
    username = models.CharField(max_length=100, verbose_name='회원아이디')
    phone_number = models.IntegerField()
=======
    username = models.CharField(max_length=100, verbose_name='회원아이디')
    name = models.CharField(max_length=30, verbose_name='이름')
    phone_number = models.CharField(max_length=15, verbose_name='전화번호')
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    university = models.CharField(db_column='University', max_length=32, blank=True, null=True)
    contents = models.CharField(max_length=300,verbose_name='세부내용',null=True,)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    status = models.CharField(max_length=30, verbose_name='상담상태',default='상담대기')

    class Meta:
        managed = False
        db_table = 'chosunconsult'


class seoulconsult(models.Model):
    id = models.AutoField(primary_key=True)
<<<<<<< HEAD
    name = models.CharField(max_length=30, verbose_name='이름')
    username = models.CharField(max_length=100, verbose_name='회원아이디')
    phone_number = models.IntegerField()
=======
    username = models.CharField(max_length=100, verbose_name='회원아이디')
    name = models.CharField(max_length=30, verbose_name='이름')
    phone_number = models.CharField(max_length=15, verbose_name='전화번호')
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    university = models.CharField(db_column='University', max_length=32, blank=True, null=True)
    contents = models.CharField(max_length=300,verbose_name='세부내용',null=True,)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    status = models.CharField(max_length=30, verbose_name='상담상태',default='상담대기')

    class Meta:
        managed = False
        db_table = 'seoulconsult'

class mainconsult(models.Model):
    id = models.AutoField(primary_key=True)
<<<<<<< HEAD
    name = models.CharField(max_length=30, verbose_name='이름')
    username = models.CharField(max_length=100, verbose_name='회원아이디')
    phone_number = models.IntegerField()
=======
    username = models.CharField(max_length=100, verbose_name='회원아이디')
    name = models.CharField(max_length=30, verbose_name='이름')
    #name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, verbose_name='전화번호')
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    university = models.CharField(db_column='University', max_length=32, blank=True, null=True)
    contents = models.CharField(max_length=300,verbose_name='세부내용',null=True,)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    status = models.CharField(max_length=30, verbose_name='상담상태',default='상담대기')

    class Meta:
        managed = False
        db_table = 'mainconsult'

class Status(models.Model):
    STATUS_CHOICES = (
        ('상담완료', 'success'),
        ('상담실패', 'fail'),
<<<<<<< HEAD
        ('상담대0', 'wait')
=======
        ('상담대기', 'wait')
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 현 계정의 사용자를 가져올 수 있음.
    nickname = models.CharField(max_length=64,verbose_name='닉네임')
    phone_number = models.CharField(max_length=12,verbose_name='전화번호')
    university = models.CharField(max_length=32,verbose_name='대학교',null=True)
    profile_photo = models.ImageField(blank=True,verbose_name='프로필사진')                 # 값을 채워넣지 않아도 되는 속성.
<<<<<<< HEAD
    id = models.AutoField(primary_key=True)
=======
    id = models.AutoField(primary_key=True,null=False)
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0

    class Meta:
        managed = False
        db_table = 'main_profile'
    # class Meta:
    #     model = Profile
    #     fields = ['id', 'nickname', 'phone_number','university', 'profile_photo',]
<<<<<<< HEAD
=======

>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
