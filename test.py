
from datetime import datetime
import time

from datetime import datetime
date_time_str = '23-03-21 01:55:19'
date_time_obj = datetime.strptime(date_time_str, '%d-%m-%y %H:%M:%S')
# print(date_time_obj)
date_obj=datetime.date(date_time_obj)
# print(date_obj)
new_date_time_obj=date_obj.strftime('%Y-%m-%d %H:%M:%S')
# print(new_date_time_obj)

DAYRUN = "2018-11-13T09:15:32"
DAYEND = "2018-11-14T02:15:32"



def floor_dt(dt, interval):
    replace = (dt.minute // interval)*interval
    return dt.replace(minute = replace, second=0, microsecond=0)



date_time_obj_run = datetime.strptime(DAYRUN, '%Y-%m-%dT%H:%M:%S')
date_obj_run=datetime.date(date_time_obj_run)

date_time_obj_end = datetime.strptime(DAYEND, '%Y-%m-%dT%H:%M:%S')
date_obj_end=datetime.date(date_time_obj_end)

if(date_obj_end > date_obj_run):
    DAYEND = date_obj_end
    print(DAYEND)
    DAYEND=DAYEND.strftime('%Y-%m-%dT%H:%M:%S')
    print(DAYEND)

