from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Task, User, Taskdetail
import re
from datetime import datetime, timedelta
from django.db.models import Q


# Create your views here.
def index(request):
    context = {}
    tasks = Task.objects.all()
    users = User.objects.values_list('name', flat=True)
    context = {
        'tasks': tasks,
        'users': users,
        'color': [
            '#FF0000', '#FF7D00', '#FFFF00', '#00FF00', '#0000FF', '#00FFFF', '#FF00FF',
        ]
    }
    return render(request, 'home.html', context)


def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 11)  # 每10任务进行分页
    page_num = request.GET.get('page', 1)  # 获取页面参数(GET请求)
    page_of_tasks = paginator.get_page(page_num)
    current_page_num = page_of_tasks.number  # 获取当前页码
    # 这里使用列表生成式生成页码区间，避免首尾取负或取到多于页码的数字
    page_range = [x for x in range(int(current_page_num)-2,int(current_page_num)+3) if 0<x<=paginator.num_pages ]
    # 加上省略标记
    if page_range[0]-1 >= 2:
        page_range.insert(0,'...')
    if paginator.num_pages - page_range[-1]>=2:
        page_range.append('...')

    #加上首尾页
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)



    context = {}
    context = {
        'page_of_tasks': page_of_tasks,
        'page_range':page_range
    }
    print(context)
    return render(request, 'tasklist.html', context)


def task_detail(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    context = {}
    # context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    # context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['task'] = task
    return render(request,'task_detail.html',context)
