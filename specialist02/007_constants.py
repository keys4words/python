class Math3D:
    PI = 3.14
    @staticmethod
    def cos(n):
        pass
    @staticmethod
    def sin(n):
        pass

from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)


import random
class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex.upper()
        self.status = None
    def wedding(self, human):
        if isinstance(human, Human):
            self.status = human
            human.status = self
        else:
            raise TypeError('object is NOT Human')
    def __add__(self, human):
        if isinstance(human, Human):
            self.status = human
            human.status = self
        else:
            raise TypeError('object is NOT Human')
    def make_children(self, partner):
        if self.status == partner and self.sex != partner.sex:
            return Human('', random.choice(['M', 'F']))
        else:
            raise Exception('This couple cannot have children')

    def __mul__(self, partner):
        if self.status == partner and self.sex != partner.sex:
            return Human('', random.choice(['M', 'F']))
        else:
            raise Exception('This couple cannot have children')
    def __repr__(self):
        return f'{self.name} [{self.sex}] status - {self.status.name}'



john = Human('John', 'm')
mike = Human('Mike', 'm')
james = Human('James', 'm')
ann = Human('Ann', 'f')
sara = Human('Sara', 'f')
# john.wedding(ann)
john + ann
print(john)
# baby = john.make_children(ann)
baby = john * ann
# print(baby)
# baby1 = john.make_children(sara)
mike + james
print(mike)
# mike.make_children(james)
