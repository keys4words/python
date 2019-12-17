class Turtle:
    def __init__(self):
        self.__private = 0

    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, value):
        self.__private = value

t1 = Turtle()
print(t1.private)
t1.private = 1435
print(t1.private)
