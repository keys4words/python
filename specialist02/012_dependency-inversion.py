#problem
# class FileRead:
#     def __init__(self, name):
#         self.__name = name
#     def read(self):
#         print(f'Read from file {self.__name}')
#         return 'File was written'
#
# class KeyboardRead:
#     def readln(self):
#         print('Read from keyboard')
#         return 'Input from keyboard was done'
#
# class SendMessage:
#     def send(self, msg):
#         print(f'Send message: {msg}')
#
# class Processing:
#     def __init__(self, read, send):
#         if not isinstance(read, FileRead):  #one level classes, this instance depending from realization of FileRead
#             raise TypeError('Error at reading from file')
#         if not isinstance(send, SendMessage):
#             raise TypeError('Error at sending message')
#         self.__reader = read
#         self.__sender = send
#     def process(self):
#         msg = self.__reader.read()
#         self.__sender.send(msg)

# f = FileRead('file.txt')
# s = SendMessage()
# p = Processing(f, s)
# p.process()

#correct
import abc

class IReader(abc.ABC):
    @abc.abstractmethod
    def read(self):
        pass

class IWriter(abc.ABC):
    @abc.abstractmethod
    def write(self, msg):
        pass

class FileRead(IReader):
    def __init__(self, name):
        self.__name = name
    def read(self):
        print(f'Read from file {self.__name}')
        return 'File was written'

class KeyboardRead(IReader):
    def read(self):
        print('Read from keyboard')
        return 'Input from keyboard was done'

class OutputNetwork(IWriter):
    def write(self, msg):
        print(f'Write message: {msg}')

class Processing:
    def __init__(self, input, output):
        if not isinstance(input, IReader):
            raise TypeError('Error at reading from file')
        if not isinstance(output, IWriter):
            raise TypeError('Error at writing message')
        self.__reader = input
        self.__sender = output
    def process(self):
        msg = self.__reader.read()
        self.__sender.write(msg)


kbd = KeyboardRead()
net = OutputNetwork()
proc = Processing(kbd, net)
proc.process()