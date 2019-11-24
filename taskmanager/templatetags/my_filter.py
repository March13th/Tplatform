from django import template
import re
from taskmanager.models import Taskdetail

register = template.Library()

@register.filter()
def endingtime_reformat(value):
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