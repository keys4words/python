class CoffeeToHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeeCup:
    def __init__(self, temp):
        self.__temp = temp

    def drink_coffee(self):
        if self.__temp > 85:
            print('Coffee Too Hot')
            # raise ValueError('Coffee Too Hot')
            raise CoffeeToHotException('Coffee Too Hot')
        elif self.__temp < 65:
            print('Coffee Too Cold')
            # raise Exception('Coffee Too Hot')
            raise CoffeeToHotException('Coffee temperature: ' + str(self.__temp))
        else:
            print('Coffee OK')

cup = CoffeeCup(50)
cup.drink_coffee()