class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def area(self):
        return self.__width * self.__height

rect1 = Rectangle(20, 40)
rect2 = Rectangle(30, 10)

# rect1.height = 20
# rect2.height = 30
#
# rect1.width = 40
# rect2.width = 10

print(rect1.area())
print(rect2.area())