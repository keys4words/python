def decorator_x(func):
    def wrapper_func():
        print('X'*20)
        func()
        print('X'*20)

    return wrapper_func
def decorator_y(func):
    def wrapper_func():
        print('Y'*20)
        func()
        print('Y'*20)

    return wrapper_func
# @decorator_y
# @decorator_x
def say_hello():
    print('Hello ')

hello = decorator_y(decorator_x(say_hello))
hello()
# say_hello()

def decorator_divide(func):
    def wrapper_func(a, b):
        print('divide', a, 'at', b)
        if b == 0:
            print('division with zero is not allowed')
            return
        return a / b
    return wrapper_func

@decorator_divide
def divide(x, y):
    return x / y

print(divide(15, 0))

from time import time
def timing(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('Elapsed time: {}'.format(end-start))
        return result
    return wrapper_func

@timing
def my_func(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

print(my_func(2000000))