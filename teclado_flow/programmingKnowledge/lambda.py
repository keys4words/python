from functools import reduce

def double(x):
    return x * 2

def add(x, y):
    return x + y

def product(x, y, z):
    return x * y * z

double = lambda x: x*2
add = lambda x, y: x+y
product = lambda x, y, z: x*y*z
print(double(4))
print(add(3, 1))
print(product(3,2,6))

a = [2, 4, 6, 7, 8, 9, 12, 34, 45]
a2 = [1, 3, 5, 6, 1, 9, 12, 11, 50]
res = map(lambda x: x*10, a)
res2 = map(lambda x, y: x + y, a, a2)
print(list(res))
print(list(res2))

res3 = filter(lambda x: x%2!=0, a)
res4 = filter(lambda x: True if x > 10 else False, a2)
print(list(res3))
print(list(res4))

e = reduce(lambda x, y: x+y, a2)
print(e, sum(a2))