class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @staticmethod
    def static_method():
        return Person.count

    @classmethod
    def class_method(cls):
        return cls.count


person = Person('Max')
person1 = Person('Max')
person2 = Person('Max')
print(person.legs, person.name)
print(Person.legs, 'number of persons =', Person.count)