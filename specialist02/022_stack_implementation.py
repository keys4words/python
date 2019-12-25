#   stack
# push(item), pop()
# peek()
# is_empty(), size()
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

s = Stack()
print(s.is_empty())
print(s.size())
s.push(43)
s.push(3)
s.push(6)
s.push(8990)
s.show()
print(s.pop())
print(s.pop())
print(s.pop())

#using Stack for palindrome
# def is_palindrom(word):
#     word = word.lower().replace(' ', '')
#     rword = ''
#     stack = Stack()
#     for char in word:
#         stack.push(char)
#     while not stack.is_empty():
#         rword += stack.pop()
#     return word == rword
#
# print(is_palindrom('привет'))
# print(is_palindrom('наган'))
# print(is_palindrom('а роза упала на лапу Азора'))

def brackets_checker(s):
    stack = Stack()
    o_allowed = '([{'
    c_allowed = ')]}'

    def matches(o, c):
        try:
            return o_allowed.index(o) == c_allowed.index(c)
        except:
            return False

    for char in s:
        if char in o_allowed:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            else:
                if not matches(stack.pop(), char):
                    return False
    if stack.is_empty():
        return True
    return False

print(brackets_checker('(()(()))'))
print(brackets_checker('(()(())'))

# using Stack for converter digit to digit at other number systems
import math
def converter(dec, base=2):
    allowed = '0123456789ABCDEF'
    stack = Stack()
    while dec > 0:
        stack.push(dec%base)
        dec = math.floor(dec/base)
    s = ''
    while not stack.is_empty():
        # s += str(stack.pop())
        s += allowed[stack.pop()]
    return s

print(converter(196, 2))
print(converter(196, 8))
print(converter(196, 16))

import string
print(string.hexdigits)

# recursion on Stack
def fact(num):
    stack = Stack()
    while num > 1:
        stack.push(num)
        num -= 1
    product = 1
    while stack.size() > 0:
        product *= stack.pop()

    return product

print(fact(5))