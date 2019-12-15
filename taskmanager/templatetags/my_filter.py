from django import template
import re
from taskmanager.models import Taskdetail,Task
import datetime

register = template.Library()

@register.filter()
def time_reformat(value):
    if isinstance(value,datetime.date):
        value = value.strftime('%Y-%m-%d')
        value_split = value.split('-')
    else:
        value_split = re.sub('\D', ',', value).split(',')
    value_reformat = '{},{},{}'.format(value_split[0], int(value_split[1]) - 1,
                                       value_split[2])
    return value_reformat

@register.filter()
def task_days(value):
    try:
        t_d_start_time = Taskdetail.objects.filter(rwh=value).values('begantime').order_by('begantime')
        t_d_end_time = Taskdetail.objects.filter(rwh=value).values('endtime').order_by('endtime')
        keep_days = (list(t_d_end_time)[-1]['endtime'] - list(t_d_start_time)[-1]['begantime']).days
    except:
        return 0
    return keep_days

@register.filter()
def for_pri_task(value):
    rwh_split = value.split('-')
    mode = rwh_split[0]
    product = rwh_split[1]
    year = rwh_split[2]
    id = rwh_split[3]
    task_object = Task.objects.get(mode=mode,product=product,year=year,id=id)
    return task_object.name

@register.filter()
def strip_space(value):
    if value:
        value = value.strip()
        return value

@register.filter()
def late(value):
    time_list =[int(t) for t in value.split(',')]
    task_endtime = datetime.datetime(year=time_list[0],month=time_list[1],day=time_list[2])
    now = datetime.datetime.today()
    late_value = (task_endtime-now).days
    return late_value