class TimeAmount:
    def __init__(self, delta):
        self._delta = delta

    def get_length(self):
        return self._delta

    def enough_for(self, another_delta):
        return self.get_length() >= another_delta