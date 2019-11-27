from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('task_list/',views.task_list,name='task_list'),
    path('task_detail/',views.task_detail,name='task_detail'),
    path('private_task/',views.private_task,name='private_task'),

]