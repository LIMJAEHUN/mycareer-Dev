from django.contrib import admin
from django.urls import path
from . import views

app_name='profile2'

urlpatterns = [
    path('<int:id>/',views.profile, name="profile"),
]