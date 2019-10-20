
class Dog:
    """Простой класс собаки"""

    def __init__(self, name, age):
        """Инициализируем атрибуты и создаем экземпляр класса"""
        self.name = name
        self.age = age
        # print('Dog created')

    def sit(self):
        """Собака будет садиться по-команде"""
        print(self.name.title() + " sit")

    def jump(self):
        """Собака прыгает"""
        print(self.name.title() + " jumped")

dog1 = Dog('Tarzan', 9)
dog1.sit()
dog1.jump()