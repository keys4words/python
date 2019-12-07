from datetime import datetime

class BeginEndMixin:
    DEFAULT_BEGIN = datetime(1970, 1, 1)

    @classmethod
    def _get_default_begin(cls):
        return cls.DEFAULT_BEGIN

    @classmethod
    def _get_default_end(cls):
        return datetime.now()

class TimeInterval(BeginEndMixin):
    def __init__(self, begin=None, end=None):
        if begin is None:
            begin = self._get_default_begin()
        if end is None:
            end = self._get_default_end()
        self._begin = begin
        self._end = end

interval = TimeInterval()
print(interval._begin)
print(interval._end)