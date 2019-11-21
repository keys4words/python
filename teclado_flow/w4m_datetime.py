from datetime import date, datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')


#class Date
today = date.today()
print(today)    #2019-11-18
print(today.day, today.month, today.year, today.weekday())   #day and month, year, day of week separately

#class Datetime
now = datetime.now()
now2 = datetime.today()
print(now, now2, sep='  <=>  ')
print(now.day, now.weekday(), now.month, now.hour, now.minute)
days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вск']
print(days[now.weekday()])

print('='*18)
print(now.strftime('%a'))
print(now.strftime('%A'))
print(f'Дата: {now.strftime("%A %d %m %Y %H:%M")}')
print('---------------Locale patterns--------------')
print(now.strftime('%c'))
print(now.strftime('%x'))
print(now.strftime('%X'))


print('='*18)
d1 = now + timedelta(days=2, hours=10, minutes=6)
print(d1.strftime('%c'))
