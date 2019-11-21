# def get_sum(a, b, c=0, d=1):
#     """
#     Возвращает сумму агрументов a и так далее d.
#     :param a: первый параметр
#     :type a: int
#     :param b: второй параметр
#     :type b: float
#     :param c:
#     :param d:
#     :return:
#     """
#     return a+b+c+d
#
# print(get_sum(461, 3))

# def get_sum(*args):
#     return sum(args)
#
# print(get_sum(1, 5, 10))

# def func(**kwargs):
#     print(kwargs)
#
# func(a=1, b=5, c=20)

# def f(a, x, *args, **kwargs):
#     print(a)
#     print(x)
#     print(args)
#     print(kwargs)
#
#
# f(1, 2, 3, 4, 7, one=46, two=False)

a = 5
# def f():
#     # x = 5
#     a = 10
#     a += 1
#     print(a)
#
# print(a)
# f()
# print(a)

# def f():
#     global a
#     a += 1
#
# print(a)
# f()
# print(a)

l = [1, '2', 3]
def f(l):
    return [i*2 for i in l]

print(f(l))

def f2(l):
    def get_mult(x):
        return x * 2
    return [get_mult(i) for i in l]

print(f2(l))

def f3(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2
    return [get_mult(i) for i in l if get_mult(i)]

print(f3(l))

def f4(l):
    def get_mult(x):
       return x * 2
    return list(map(get_mult, l))

print(f4(l))