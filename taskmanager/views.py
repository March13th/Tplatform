from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Task, User, Taskdetail
import re
from datetime import datetime, timedelta
from django.db.models import Q


# Create your views here.
def index(request):
    year = datetime.now().year
    context = {}
    year_tasks = Task.objects.filter(endingtime__startswith=year).filter(flag='已完成')
    year_ctctdcs = year_tasks.filter(product='CTC/TDCS')
    year_cips = year_tasks.filter(product='CIPS')
    year_bm = year_tasks.filter(product='BM')
    users = User.objects.filter(type='测试').values_list('name', flat=True)
    month_ctctdcs = [len(year_ctctdcs.filter(endingtime__contains=str(month)+'月')) for month in range(1,13)]
    month_cips = [len(year_cips.filter(endingtime__contains=str(month) + '月')) for month in range(1, 13)]
    month_bm = [len(year_bm.filter(endingtime__contains=str(month) + '月')) for month in range(1, 13)]
    for i in month_ctctdcs:
        print(i)
    context = {
        'users': users,
        'year_ctctdcs':year_ctctdcs,
        'year_cips':year_cips,
        'year_bm':year_bm,
        'month_ctctdcs':month_ctctdcs,
        'month_cips': month_cips,
        'month_bm': month_bm,
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

    users = User.objects.filter(type='测试').values_list('name', flat=True)
    context = {}
    context = {
        'page_of_tasks': page_of_tasks,
        'page_range':page_range,
        'users':users,
    }
    return render(request, 'tasklist.html', context)


def task_detail(request):
    users = User.objects.filter(type='测试').values_list('name', flat=True)
    rwh = request.GET.get('rwh')
    rwh_split = rwh.split('-')
    mode = rwh_split[0]
    product = rwh_split[1]
    year = rwh_split[2]
    id = rwh_split[3]
    Task_object = get_object_or_404(Task,mode=mode,product=product,year=year,id=id)
    Taskdetail_object = Taskdetail.objects.filter(rwh=rwh)
    context = {
        'users':users,
        'Task_object':Task_object,
        'Taskdetail_object':Taskdetail_object,
    }
    return render(request,'task_detail.html',context)


def private_task(request):
    context = {}
    username = request.GET.get('name')
    if username:
        tasks = Taskdetail.objects.filter(name=username)
    users = User.objects.filter(type='测试').values_list('name', flat=True)
    tasks_unfinished_num = Taskdetail.objects.filter(Q(name=username) & ~Q(canbegan='已完成')).count()
    context = {
        'tasks':tasks,
        'users':users,
        'username':username,
        'tasks_unfinished_num':tasks_unfinished_num,
    }
    return render(request,'private_task.html',context)


def knowledge(request):
    return render(request,'knowledge.html')