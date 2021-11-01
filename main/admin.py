from django.contrib import admin
# Register your models here.
from .models import  member,MainPost,chosunPost, seoulPost, mainconsult, chosunconsult, seoulconsult, Profile, Status
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class PostAdmin(admin.ModelAdmin):
    list_display=('id','rogophoto','postname','area','job','etc')
    list_filter = ['job', 'area']
    search_fields = ['postname']
    user_filter = ('area')



class memberAdmin(admin.ModelAdmin):
    list_display=('id' ,'title')

class consultAdmin(admin.ModelAdmin):
    list_display=('id','name','phone_number','university','contents','created_at','status')
    list_filter = ['university','created_at']
    actions = ['change_success', 'change_fail', 'change_wait']
# class pointAdmin(admin.ModelAdmin):
#     list_display=('point_id','pname')
    # admin action 추가
    def change_success(self, request, queryset):
        updated_count = queryset.update(status='상담완료') #queryset.update
        self.message_user(request, '{}건의 포스팅을 상담완료 상태로 변경'.format(updated_count)) #django message framework 활용
    change_success.short_description = '선택된 상담내역을 상담완료 상태로 변경합니다.'

    def change_fail(self, request, queryset):
        updated_count = queryset.update(status='상담실패') #queryset.update
        self.message_user(request, '{}건의 포스팅을 상담실패 상태로 변경'.format(updated_count)) #django message framework 활용
    change_fail.short_description = '선택된 상담내역을 상담실패 상태로 변경합니다.'

    def change_wait(self, request, queryset):
        updated_count = queryset.update(status='상담중') #queryset.update
        self.message_user(request, '{}건의 포스팅을 상담대기 상태로 변경'.format(updated_count)) #django message framework 활용
    change_wait.short_description = '선택된 상담내역을 상담중 상태로 변경합니다.'



class ProfileInline(admin.StackedInline): # 로또 프로젝트에서 썼던 방식으로 유저 밑에 프로필 을 붙여서 보여주려고 이를 상속받음
    model = Profile
    con_delete = False                    # 프로필을 아예 없앨 수 없게 하는 속성(한번 만들면 지우는건 이상하니까)

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(seoulPost, PostAdmin)
admin.site.register(chosunPost, PostAdmin)
admin.site.register(mainconsult, consultAdmin)
admin.site.register(chosunconsult, consultAdmin)
admin.site.register(seoulconsult, consultAdmin)
admin.site.register(MainPost, PostAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
