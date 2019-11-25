from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4


# shape = Shape()
square = Square(10)
print(square.area())
print(square.perimeter())