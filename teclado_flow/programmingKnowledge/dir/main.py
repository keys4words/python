from programmingKnowledge.dir.rectangle import Rectangle
from programmingKnowledge.dir.triangle import Triangle

rect = Rectangle()
tri = Triangle()

rect.set_values(2, 4)
tri.set_values(2, 4)
rect.set_color('red')
tri.set_color('green')

print(rect.area())
print(tri.area())
print(rect.get_color())
print(tri.get_color())
