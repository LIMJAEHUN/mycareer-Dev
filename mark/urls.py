from django.urls import path
from. import views

app_name = 'mark'

urlpatterns = [
    path('<int:MainPost_id>/', views.add_mark, name='add_mark'),
    #path('', views.mark, name ='markmark_detail'),
    path('mark/', views.mark, name ='markmark_detail'),
    path('<int:MainPost_id>/delete', views.delete, name= 'delete'),
]
