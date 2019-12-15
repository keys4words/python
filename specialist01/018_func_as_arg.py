def sum_range_of_func(start, end, func):
    n = 0
    for i in range(start, end+1):
        n += func(i)
    return n

def f(index): return index ** 2

print(sum_range_of_func(0, 10, f))
print(sum_range_of_func(0, 10, lambda i: i**2))


lst = [1, 3, 56, 67, 77, 67, 77, 122]
print(list(map(lambda el: el//2, lst)))

print(set(filter(lambda i: i>55, lst)))

from functools import reduce
lst = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a+b, lst, 100))

lst = [6, 3, 7, 2, 6, 9, 4, 8]
print(reduce(lambda a, b: a if a>b else b, lst))

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = 'yzdajslf'
c = (None, True, True, False, True, False, False)
z = list(zip(a, b, c))
print(z)

lst = [6, 3, 7, 2, 6, 9, 4, 8]
print(list(map(lambda x: x*10, list(filter(lambda x: x>5, lst)))))

def compose(f,g):
    return lambda x: f(g(x))

double = lambda x: 2*x
inc = lambda x: x+1
print(double(3))
print(inc(3))
inc_and_double = compose(inc, double)
inc_and_double2 = lambda x: inc(double(x))

print(inc_and_double(3), inc_and_double2(3))