import abc
from random import randrange

class IShape(abc.ABC):
    @abc.abstractmethod
    def get_perimeter(self):
        pass
    @abc.abstractmethod
    def get_area(self):
        pass
    @abc.abstractmethod
    def get_description(self):
        pass

class Circle(IShape):
    PI = 3.14
    def __init__(self, radius):
        self.__radius = radius
    def get_perimeter(self):
        return 2*Circle.PI*self.__radius
    def get_area(self):
        return Circle.PI*self.__radius**2
    def get_description(self):
        return f'Circle with radius: {self.__radius}'

class Rectangle(IShape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    def get_width(self):
        return self.__width
    width = property(get_width)
    def get_height(self):
        return self.__height
    height = property(get_height)
    def get_perimeter(self):
        return 2*(self.__width + self.__height)
    def get_area(self):
        return self.__width * self.__height
    def get_description(self):
        return f'Rectangle with width: {self.__width} and height: {self.__height}'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def get_description(self):
        return f'Square with side: {self.width}'

class Game:
    QUESTION_COUNT = 2
    def __init__(self):
        raise Exception('Cannot istanciate this class')
    @staticmethod
    def __get_shape():
        type = randrange(3)
        if type == 0:
            return Circle(randrange(1, 10))
        if type == 1:
            return Rectangle(randrange(1, 10), randrange(1, 10))
        if type == 2:
            return Square(randrange(1, 10))
    @staticmethod
    def __calculate(string, answer):    #string - area or perimeter
        while True:
            guess = input(f'Input my {string} for this figure: ').strip()
            if not guess.replace('.', '', 1).isdigit():
                print('Your input must be digits')
                continue
            break
        if float(guess) == answer:
            print('Correct!')
        else:
            print(f'Error! Right answer is {answer}')


    @classmethod
    def __run(cls):
        shape = cls.__get_shape()
        if isinstance(shape, IShape):
            print(shape.get_description())
            cls.__calculate('Area', shape.get_area())
            cls.__calculate('Perimeter', shape.get_perimeter())
        else:
            raise TypeError('Undefined type of figure!')
    @classmethod
    def play(cls):
        print(f'Hey! We are figures and you have {cls.QUESTION_COUNT} questions')
        while True:
            is_game_over = input('Play? y/n ').strip()
            if is_game_over.upper() == 'N':
                break
            cls.__run()
        print('Thank you! Bye!')

Game.play()
