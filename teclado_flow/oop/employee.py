class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # def __repr__(self):
    #     return self.fullname() + ' -> ' + str(self.pay)

    def __str__(self):
        return self.fullname() + ' - ' + str(self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Shultz', 50000)
emp_2 = Employee('Joe', 'Dow', 10000)

# emp_1.apply_raise()
# print(emp_1.pay, emp_1.fullname())

print(len('test'))
print('test'.__len__())
print(len(emp_1))

print(emp_1+emp_2)

# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('1','2'))