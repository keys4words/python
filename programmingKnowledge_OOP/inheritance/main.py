from inheritance.rectangle import Rectangle
from inheritance.triangle import Triangle

rect = Rectangle()
tri = Triangle()
rect.set_values(50, 30)
tri.set_values(40, 60)
rect.set_color('red')
tri.set_color('blue')
print(rect.area(), rect.get_color())
print(tri.area(), tri.get_color())
