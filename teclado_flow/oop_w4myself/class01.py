# class A:
#     property1 = 'Property 1'
#     property2 = 'Property 2'
#     name = 'guest'
#
#     def say_hi(self, name=''):
#         if name:
#             return 'Hi, ' + name
#         else:
#             return 'Hello, ' + self.name
#
# a = A()
# b = A()
# # a.property1 = 'Property 1'
# # a.property2 = 'Property 2'
# print(a)
# print(a.property1, a.property2)
# print(b.say_hi('John'))
# print(b.say_hi())

from oop_w4myself.classes import Person, Employee
# person1 = Person('Max')
# person1.print_info()

person2 = Person('James')
# print(person2._Person__age)
# person2.set_age(140)
person2.age = 35
person2.print_info()

employee = Employee('Ioan', 15, 'Yandex')
# employee.print_info()
# employee.more_info()
print(employee)

