from timeAmount import TimeAmount
class TimeInterval(TimeAmount):
    def __init__(self, begin, end):
        self._begin = begin
        self._end = end

    # def get_begin(self):
    #     return self._begin
    #
    # def get_end(self):
    #     return self._end

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        self._begin = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    def get_length(self):
        return self._end-self._begin


    def __repr__(self):
        return 'TimeInterval({}, {})'.format(repr(self._begin), repr(self._end))

    def __str__(self):
        return '{} -> {}'.format(self._begin, self._end)