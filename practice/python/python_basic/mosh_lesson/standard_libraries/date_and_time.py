# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : date_and_time.py
# @Date         : 2023/11/5 18:49
#
# @Description  :
#

import time
from datetime import datetime, timedelta

print(time.time())  # 1970-1-1 到现在的秒数
dt = datetime(2020, 1, 1)
print(dt)
dt = datetime.now()
print(dt)
dt = datetime.strptime("2022/01/01", "%Y/%m/%d")
print(dt)
dt = datetime.fromtimestamp(time.time())
print(dt)
print(dt.strftime("%Y-%m-%d"))
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print(dt.strftime("%y-%m-%d"))

birthday = datetime.strptime("1988/02/13", "%Y/%m/%d")
now = datetime.now()
duration = now - birthday
print(duration)
print("age: ", duration.days // 365)

week_ago = datetime.now() - timedelta(days=7)
print(week_ago.strftime("%Y-%m-%d"))
