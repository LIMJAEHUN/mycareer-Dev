from django.urls import path
from. import views

app_name = 'mark'

urlpatterns = [
    path('<int:MainPost_id>/', views.add_mark, name='add_mark'),
<<<<<<< HEAD
    #path('', views.mark, name ='markmark_detail'),
    path('mark/', views.mark, name ='markmark_detail'),
    path('<int:MainPost_id>/delete', views.delete, name= 'delete'),
=======
    #path('', views.mark_detail, name='mark_detail'),
    path('<int:MainPost_id>/delete', views.delete, name= 'delete'),
    path('mark/', views.mark, name ='mark'),
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
]
