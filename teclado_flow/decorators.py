# def hello():
#     return "hello, I am func 'hello'"
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "hello, I am func 'hello'"
#
# test = hello
#
# print(test())

# def my_decorator(func):
#     def wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrapper
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')


# test = my_decorator(func_test)
# test()
# func_test()

def make_title(func):
    def wrapper():
        title = func()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapper

@make_title
def hi():
    return 'hello, world'

print(hi())
