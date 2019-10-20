class Car:
    def __init__(self, a=40):
        self.speed = a

    def get_speed(self):
        return self._speed

    def set_speed(self, a):
        if a <= 0 or a >= 200:
            print("speed needs to be between 0 to 200")
        else:
            self._speed = a
    speed = property(get_speed, set_speed)



car1 = Car()
# car1.set_speed(-60)
# print(car1.get_speed())
print(car1.speed)