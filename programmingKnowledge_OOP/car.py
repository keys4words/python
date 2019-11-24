class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Car(200, 'red')
honda = Car(220, 'blue')
audi = Car(250, 'black')

ford.set_speed(343)
# ford.speed = 400
print(ford.get_speed(), ford.get_color())
