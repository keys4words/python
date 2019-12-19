class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'I\'m {self.name}'


class Student(Person):
    pass

person = Person('Max')
student = Student('John')
print(person, isinstance(person, Person))
print(student, isinstance(student, Person))
print(issubclass(Student, Person))
print(issubclass(Student, list))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_to(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'I\'m point: {self.x}x{self.y}'

class Point3D(Point):
    def __init__(self, x, y, z):
        # Point.__init__(self, x, y)
        super().__init__(x, y)
        self.z = z
    def move_by(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
    def move_to(self, x, y, z):
        super().move_to(x, y)
        self.z = z
    def __repr__(self):
        s = Point.__repr__(self)
        return f'{s}x{self.z}'

p = Point(10, 20)
p3d = Point3D(30, 40, 50)
# print(p3d, p3d.x, p3d.y)
p.move_to(100, 200)
p3d.move_by(300, 400, 500)
print(p, p3d)




