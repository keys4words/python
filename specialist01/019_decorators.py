def add_underscores(par):
    def decor(fn):
        def wrapper(name):
            s = '_' + fn(name) + '_'
            s += '\n' + par
            return s
        return wrapper
    return decor

@add_underscores('=============')
def hello(name):
    return 'hello, ' + name

# @add_underscores
def oops():
    return 'oops'


print(hello('Max'))
# text = add_underscores(hello)
# print(text())
print(oops())

import functools

@functools.lru_cache(maxsize=32)
def square(n):
    print('here')
    return n**2

print(square(4))
print(square(4))
print(square(4))
print(square(4))