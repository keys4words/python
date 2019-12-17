class Person:
    legs = 2
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def show(self):
        pass

person = Person('Max')
person1 = Person('Max')
person2 = Person('Max')
print(person.legs, person.name)
print(Person.legs, 'number of persons =', Person.count)