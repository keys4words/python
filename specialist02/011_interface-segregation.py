import abc

# wrong
# class IBird(abc.ABC):
#     @abc.abstractmethod
#     def eat(self):
#         pass
#
#     @abc.abstractmethod
#     def go(self):
#         pass
#
#     @abc.abstractmethod
#     def sound(self):
#         pass
#
#     @abc.abstractmethod
#     def fly(self):
#         pass

#   correct
class IBird(abc.ABC):
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def go(self):
        pass

    @abc.abstractmethod
    def sound(self):
        pass

class IFlyingBird(IBird):
    @abc.abstractmethod
    def fly(self):
        pass

def go_fly(bird):
    if isinstance(bird, IFlyingBird):
        distance = bird.fly()
        print(distance)

class Falcon(IFlyingBird):
    def eat(self):
        print(self.__class__.__name__ + ' eat')

    def go(self):
        print(self.__class__.__name__ + ' go')

    def sound(self):
        print(self.__class__.__name__ + ' sound')

    def fly(self):
        print(self.__class__.__name__ + ' fly')


falcon = Falcon()
go_fly(falcon)

class Ostrich(IBird):
    def eat(self):
        print(self.__class__.__name__ + ' eat')

    def go(self):
        print(self.__class__.__name__ + ' go')

    def sound(self):
        print(self.__class__.__name__ + ' sound')

ostrich = Ostrich()
ostrich.eat()
go_fly(ostrich)