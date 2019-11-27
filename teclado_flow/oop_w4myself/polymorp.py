from oop_w4myself.classes import Person, Employee

person = Person('Katy', 30)
person.age = 34
person.print_info()

employee = Employee('Nick', 30, 'Rinova')
employee.print_info()
print(employee)