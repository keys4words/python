from abc import ABCMeta, abstractmethod

class AbstractTimeAmount(metaclass=ABCMeta):
    @abstractmethod
    def get_length(self):
        pass

    def enough_for(self, another_delta):
        return self.get_length() >= another_delta