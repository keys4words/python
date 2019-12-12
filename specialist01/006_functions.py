def seconds_per_day(days=10):
    res = 24 * days * 3600
    return res


print(seconds_per_day(3))
print(seconds_per_day())

def area_of_circle(radius):
    return 3.14*radius**2


def area_of_disc(outer, inner):
    '''
    Return area of disk
    :param outer: outer radius
    :param inner: inner radius
    :return: area
    '''
    return area_of_circle(outer)-area_of_circle(inner)


print(area_of_disc(10, 3))

# x = 10
# def fn():
#     global x
#     print(x)
#     x = 20
#     print(x)
#
# print(x)
# fn()
# print(x)

def fn(a, b=2, c=3):
    pass

fn(c=30, a=10)


def fun(*params):
    # print(type(params))
    for el in params:
        print(el, end=' ')

fun(1,2, 3, 5, 'a')
print()
print('*'*12)

def fun2(**varags):
    for k, v in varags.items():
        print(k, v)

fun2(John=24, Pete=44)

print('*'*12)
def func_outer():
    x = 2
    print('x equals', x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Local x changed into', x)

func_outer()
