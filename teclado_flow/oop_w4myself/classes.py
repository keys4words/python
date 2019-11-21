class Person:
    # name = "John"

    def __init__(self, name):
        self.name = name
        self.__age = 20

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