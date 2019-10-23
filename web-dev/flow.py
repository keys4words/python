from datetime import datetime as dt
from datetime import timedelta

now = dt.now()
print(now)
# print(dt.now().day)
# print(dt.now().hour)
# print(dt.now().minute)
# print(dt.now().month)
# date1 = dt(2019, 11, 5)
date1 = now + timedelta(days=180)
print(date1)
delta = now - date1
print('diff = ', delta.days)