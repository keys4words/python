class User:
    count = 0
    def __init__(self, name, login, psw):
        self.__name = name
        self.__login = login
        self.__psw = psw
        User.count += 1
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    name = property(get_name, set_name)

    def get_login(self):
        return self.__login
    def set_login(self, login):
        raise AttributeError('Login cannot change!')
    login = property(get_login, set_login)

    def get_psw(self):
        return '*******'
    def set_psw(self, psw):
        self.__psw = psw
    psw = property(get_psw, set_psw)

    def show_info(self):
        print('='*14)
        print(f'Name: {self.__name}')
        print(f'Login: {self.__login}')


class SuperUser(User):
    count = 0
    def __init__(self, name, login, psw, role):
        super().__init__(name, login, psw)
        self.__role = role
        SuperUser.count += 1
        User.count -= 1

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role):
        self.__role = role

    def show_info(self):
        super().show_info()
        print(f'Role: {self.__role}')

user1 = User('Paul McCartney', 'paul', '1234')
user2 = User('George Harrison', 'george', '5668')
user3 = User('Richard Starkey', 'ringo', '9526')
admin = SuperUser('John Lennon', 'john', '0000', 'admin')

user3.show_info()
print(user3.psw)
# user3.set_login('ringo5')
admin.show_info()
users = User.count
print(f'Всего обычных пользователей: {users}')
admins = SuperUser.count
print(f'Всего админов: {admins}')

