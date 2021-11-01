from django.contrib import admin
from django.urls import path
from . import views
# index는 대문, blog는 게시판
from main.views import index, blog, posting, remove_post, login, signup, Consult, profile, consult2,change_profile, success
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import include


app_name='main'


urlpatterns = [
    path('index',index),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup2/', views.signup2, name='signup2'),
    path('<int:id>blog/',blog),
    path('success/',views.success, name='success'),
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/',posting, name="posting"),
    path('blog/<int:pk>/remove/', remove_post),
    path('search',views.search, name='search'),
    path('add/' ,views.blog),
    #상담하기 페이지
    path('Consult/<point_id>/', views.Consult, name='Consult'),
    #프로필 페이지
    path('<int:id>/profile', views.profile, name="profile"),
    path('<str:username>/change_profile', views.change_profile, name="change_profile"),
    #상담하기 게시판
    path('consult2', views.consult2, name='consult2'),
    path('consult2/<int:pk>/', views.consult2_popup, name='consult2_popup'),
    path('nopage/',views.nopage, name='nopgae'),
    #ckeditor 관련 url
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
