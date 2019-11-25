import math

class Number:
    def __init__(self, num):
        self.num = num

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, other):
        return Circle(self.__radius + other.__radius)

    def __lt__(self, other):
        return self.__radius < other.__radius

    def __gt__(self, other):
        return self.__radius > other.__radius

    def __str__(self):
        return f"Circle with radius {self.__radius} with area {self.area()}"


n1 = Number(1)
n2 = Number(2)
# print(n1+n2)

c1 = Circle(2)
c2 = Circle(3)
c3 = c1 + c2
print(c3)
print(c2>c1)