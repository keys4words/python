from inheritance.polygon import Polygon
from inheritance.shape import Shape

class Rectangle(Polygon, Shape):
    def area(self):
        return self.get_height() * self.get_width()