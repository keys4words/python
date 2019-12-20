#problem - too long constructor - telescope
# class Pizza:
#     def __init__(self, size, cheese, pepperoni, bacon):
#         self.__size = size
#         self.__cheese = cheese
#         self.__pepperoni = pepperoni
#         self.__bacon = bacon
#
#     def show(self):
#         recipe = 'Pizza ' + str(self.__size) + ' with '
#         recipe += 'cheese, ' if self.__cheese else ''
#         recipe += 'pepperoni, ' if self.__pepperoni else ''
#         recipe += 'bacon' if self.__bacon else ''
#         return recipe
#
# pizza = Pizza(12, True, False, False)

#solution
class PizzaMaker:
    def __init__(self, size):
        self._size = size
        self._cheese = False
        self._pepperoni = False
        self._bacon = False
    def cheese(self):
        self._cheese = True
        return self
    def pepperoni(self):
        self._pepperoni = True
        return self
    def bacon(self):
        self._bacon = True
        return self
    def make(self):
        return self

class Pizza:
    def __init__(self, maker: PizzaMaker):
        self.__size = maker._size
        self.__cheese = maker._cheese
        self.__pepperoni = maker._pepperoni
        self.__bacon = maker._bacon

    def show(self):
        recipe = 'Pizza ' + str(self.__size) + ' with '
        recipe += 'cheese, ' if self.__cheese else ''
        recipe += 'pepperoni, ' if self.__pepperoni else ''
        recipe += 'bacon' if self.__bacon else ''
        return recipe

pizza = PizzaMaker(12).cheese().bacon().make()
order = Pizza(pizza)
print(order.show())