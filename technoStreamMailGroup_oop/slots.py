from datetime import datetime

class TimeInterval:
    __slots__ = ['_begin', '_end']

    def __init__(self, begin, end):
        self._begin = begin
        self._end = end

    def get_length(self):
        return self._end - self._begin


interval = TimeInterval(datetime(2018, 1, 1), datetime(2018, 1, 2))
# interval.xxx = 123
# print(interval, interval.xxx)
print(interval.get_length())