class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_method(self):
        print(self.a)
        print(self._b)
        print(self.__c)
        print('public method')
        self.__private_method()

    def __private_method(self):
        print('private method')


inst = Hello('Max')
# print(inst.a)
# print(inst._b)
inst.public_method()
# inst.__private_method()