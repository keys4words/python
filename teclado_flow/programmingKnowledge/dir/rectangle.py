from programmingKnowledge.dir.polygon import Polygon
from programmingKnowledge.dir.shape import Shape

class Rectangle(Polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height()