from datetime import datetime, timedelta
from timeInterval import TimeInterval
from timeAmount import TimeAmount

interval = TimeInterval(
    datetime(year=2018, month=12, day=5),
    datetime(year=2019, month=12, day=5)
)
# print(interval.get_begin())
# print(interval.begin)
# interval.begin = 2
# print(interval.begin)
# print(interval)

# amount = TimeAmount(timedelta(seconds=43))
# print(amount.enough_for(timedelta(seconds=36)))
# print(amount.enough_for(timedelta(seconds=56)))
amount = TimeInterval(datetime(2018, 1, 1), datetime(2018, 1, 2))
print(amount)
print(amount.enough_for(timedelta(seconds=32)))