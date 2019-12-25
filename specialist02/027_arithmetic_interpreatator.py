import abc
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
    def clear(self):
        self.__data = list()
    def show(self):
        print('\n'.join(str(v) for v in self.__data))

class InterpretatorAbstract(abc.ABC):
    def __init__(self, code):
        self.code = code
    def execute(self):
        return self._parse()
    @abc.abstractmethod
    def _parse(self):
        pass
    @abc.abstractmethod
    def _evaluate(self, code):
        pass

import enum
class Token(enum.Enum):
    PLUS = '+',
    MINUS = '-',
    ASTERISK = '*',
    SLASH = '/',
    CARET = '^',
    BRACKET_OPEN = '(',
    BRACKET_CLOSE = ')',
    def __eq__(self, other):
        if type(other) is str:
            return self.value[0] == other


class Interpreter(InterpretatorAbstract):
    def __init__(self, file=None, string=None):
        if string is not None:
            self.__code = string
        else:
            if file is None:
                raise TypeError('Input code in string format or in file')
            with open(file) as f:
                self.__code = f.read()
        self.__ops = Stack()
        self.__vals = Stack()
    def execute(self):
        return self._parse()
    def _parse(self):
        lines = self.__code.strip().split('\n')
        res = list()

        for line in lines:
            if not self._validate(line):
                raise Exception("Bugs in code with brackets!")

        for line in lines:
            line = ''.join(line.split())
            res.append(self._evaluate(line))
        return res
    def _validate(selfs, code):
        stack = Stack()
        for char in code:
            if char == '(':
                stack.push(char)
            elif char == ')':
                stack.pop()
        if stack.is_empty():
            return True
        else:
            return False
    def _evaluate(self, code):
        operators = ['+', '-', '*', '/', '^']
        code = '(' + code + ')'
        prev_char = ''
        for char in code:
            if char.isdigit():
                prev_char += char
                continue
            elif prev_char != '':
                self.__vals.push(prev_char)
                prev_char = ''
            if char == Token.BRACKET_OPEN:
                continue
            elif char in operators:
                self.__ops.push(char)
            elif char == Token.BRACKET_CLOSE:
                op = self.__ops.pop()
                v = int(self.__vals.pop())
                if op == Token.PLUS:
                    v = int(self.__vals.pop()) + v
                elif op == Token.MINUS:
                    v = int(self.__vals.pop()) - v
                elif op == Token.ASTERISK:
                    v = int(self.__vals.pop()) * v
                elif op == Token.SLASH:
                    v = int(self.__vals.pop())//v
                elif op == Token.CARET:
                    v = int(self.__vals.pop()) ** v
                self.__vals.push(v)
                continue
            else:
                self.__vals.push(char)
        return self.__vals.pop()

# interpreter = Interpreter('(1+((2+3)*(4*5)))')
interpereter = Interpreter(file='operations.txt')
print(interpereter.execute())

# interpreter = Interpreter('(2+((2*3)/(4^5)))')
# print(interpreter.execute())