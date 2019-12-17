class Point:
    __counter = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point.__counter += 1
    @classmethod
    def get_counter(cls):
        return cls.__counter

    def move_to(self, x, y):
        self.__x = x
        self.__y = y
    def move_by(self, x, y):
        self.__x += x
        self.__y += y
    def __repr__(self):
        return f'I\'m point: {self.__x}x{self.__y}'
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self, x):
        self.__x = x
    x = property(get_x, set_x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


