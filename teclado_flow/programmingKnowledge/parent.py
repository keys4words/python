class Parent:
    def __init__(self, name):
        print('Parent constructor', name)

class Parent2:
    def __init__(self, name):
        print('Parent2 constructor', name)

class Child(Parent2, Parent):
    def __init__(self):
        print('Child constructor')
        Parent2.__init__(self, 'Max')
        Parent.__init__(self, 'Tom')


child = Child()
print(Child.__mro__)