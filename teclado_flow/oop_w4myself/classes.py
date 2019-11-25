class Person:
    # name = "John"

    def __init__(self, name, age=20):
        self.name = name
        self.__age = age

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, age):
    #     if age in range(1, 101):
    #         self.__age = age
    #     else:
    #         print("age is default")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 101):
            self.__age = age
        else:
            print("age is default")

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')



class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def print_info(self):
        super().print_info()
        print(f'Work: {self.company}')

    def more_info(self):
        print(f'Name: {self.name} works in {self.company}')

    def __str__(self):
        return f'Name: {self.name} works in {self.company}'