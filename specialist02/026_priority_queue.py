class Queue:
    def __init__(self):
        self.__data = list()
    def enqueue(self, item):
        self.__data.append(item)
    def dequeue(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)
        return None
    def rear(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data)-1]
        return None
    def front(self):
        if len(self.__data) > 0:
            return self.__data[0]
        return None
    def is_empty(self):
        return len(self.__data) == 0
    def size(self):
        return len(self.__data)
    def clear(self):
        self.__data = list()
    def show(self):
        print(', '.join(str(v) for v in self.__data))


# в PriorityQueue нужна сортировка - либо при добавлении в очередь, либо при извлечении
class PriorityQueue(Queue):
    pass

class Client:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

q = PriorityQueue()
q.enqueue(Client('John', 2))
q.enqueue(Client('Mike', 1))