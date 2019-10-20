class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first.lower() + '.' + last.lower() + '@gmail.com'

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first.lower(), self.last.lower())

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp1 = Student('John', 'Rembo')
emp1.first = 'Jim'
emp1.fullname = 'James Bond'

print(emp1.fullname)
print(emp1.email)

del emp1.fullname

