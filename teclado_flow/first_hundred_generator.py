class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

my_gen = FirstHundredGenerator()
print(my_gen.number)
next(my_gen)
print(my_gen.number)

class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1,2,3,4,5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()