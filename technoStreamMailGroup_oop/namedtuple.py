from collections import namedtuple
from datetime import datetime

# TimeInterval = namedtuple('TimeInterval', ['begin', 'end'])
#
# interval = TimeInterval(datetime(2018, 1, 1), datetime(2018, 1, 2))
# print(interval.begin)

class TimeInterval(namedtuple('TimeInterval', ['begin', 'end'])):
    def get_length(self):
        return self.end - self.begin

interval = TimeInterval(datetime(2018, 1, 1), datetime(2018, 1, 2))
print(interval.get_length())