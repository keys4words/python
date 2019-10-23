class ListIterator:
    def __init__(self, lst):
        self.__list = lst
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__list):
            raise StopIteration
        return self.__list[self.__index]


a = [1, 9, 13, 5, 6]
mylist = ListIterator(a)
it = iter(mylist)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for i in it:
    print(i)