class Person:
    DEFAULT_NAME = 'John'
    DEFAULT_SURNAME = 'Dow'

    @classmethod
    def _get_default_name(cls):
        return cls.DEFAULT_NAME

    @classmethod
    def _get_default_surname(cls):
        return cls.DEFAULT_SURNAME

    def __init__(self, name=None, surname=None):
        if name is None:
            name = self._get_default_name()
        if surname is None:
            surname = self._get_default_surname()
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


    def __str__(self):
        return self.__name + ' ' + self.__surname

person = Person()
print(type(person), type(Person))
print(Person is type(person))
print(isinstance(person, Person))
person.xxx = 'something'
print(person, person.xxx)
print('private field', person._Person__surname)
print('class method', Person._get_default_name())

