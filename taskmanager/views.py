from django.shortcuts import render
from .models import Task,User,Taskdetail
import re
from datetime import datetime,timedelta
from django.db.models import Q

# Create your views here.
def index(request):
    context = {}
    tasks = Task.objects.all()
    users = User.objects.values_list('name',flat=True)
    context = {
        'tasks':tasks,
        'users':users,
        'color':[
            '#FF0000','#FF7D00','#FFFF00','#00FF00','#0000FF','#00FFFF','#FF00FF',
        ]
    }
    return render(request,'home.html',context)