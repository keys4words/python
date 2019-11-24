class Polygon:
    __width = None
    __height = None

    def set_values(self, width, height):
        self.__height = height
        self.__width = width

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
