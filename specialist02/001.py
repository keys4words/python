class Lamp:
    count = 0
    def __init__(self, floor=0):
        self.__state = False
        self.__floor = floor
        Lamp.count += 1
    def switch_on(self):
        if not self.state:
            print('lamp ON')
            self.__state = True
    def switch_off(self):
        if self.state:
            print('lamp OFF')
            self.__state = False

    def get_state(self):
        return self.__state
    # def set_state(self, state):
    #     self.__state = state

    state = property(get_state)

    def get_floor(self):
        return self.__floor
    def set_floor(self, floor):
        self.__floor = floor

    floor = property(get_floor, set_floor)


    def __repr__(self):
        return f'I\'m lamp at {self.floor} floor'


l1 = Lamp(1)
l2 = Lamp(2)
l3 = Lamp(3)
print(isinstance(l1, Lamp))
l1.switch_on()
l1.switch_off()
print(l2.state, l1.floor)
print(l3)
l4 = Lamp(1)

print(Lamp.count)
print(l2.__class__)