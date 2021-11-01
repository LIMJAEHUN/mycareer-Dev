from django.urls import path
from. import views

app_name = 'mark'

urlpatterns = [
    path('<int:MainPost_id>/', views.add_mark, name='add_mark'),
    #path('', views.mark_detail, name='mark_detail'),
    path('<int:MainPost_id>/delete', views.delete, name= 'delete'),
    path('mark/', views.mark, name ='mark'),
]
