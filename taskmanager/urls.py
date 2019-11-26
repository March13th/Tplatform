from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('tasklist/',views.task_list,name='tasklist'),
    path('<path:task_pk>',views.task_detail,name='task_detail'),

]