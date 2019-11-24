class Hello:
    def __init__(self):
        # self.name = name
        # self.age = 10
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_method(self):
        # print(self.a)
        # print(self.__c)
        print('public')
        self.__private_method()

    def __private_method(self):
        print('private')


hello = Hello()
print(hello.a)
print(hello._b)
hello.public_method()
# print(hello.__c)