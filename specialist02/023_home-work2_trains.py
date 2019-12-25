class Stack:
    def __init__(self):
        self.__data = list()
    def push(self, item):
        self.__data.append(item)
    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
        return None
    def peek(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data)-1]
        return None
    def is_empty(self):
        return len(self.__data) == 0
    def size(self):
        return len(self.__data)
    def show(self):
        print('\n'.join(str(v) for v in self.__data))



def do_lab(train):
    dock = Stack()
    train = train.split()
    train = list(map(int, train))
    needed = 1

    for wagon in train:
        dock.push(wagon)
        if wagon == needed:
            dock.pop()
            needed += 1
        while dock.size() > 0:
            if dock.peek() == needed:
                dock.pop()
                needed += 1
            else:
                break
    if dock.is_empty():
        print('Вывели')
    else:
        print('Неудача')




while True:
    nums = input('Введите номера вагонов: ')
    if nums == '0':
        break
    do_lab(nums)