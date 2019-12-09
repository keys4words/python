def seconds_per_day(days=10):
    res = 24 * days * 3600
    return res


print(seconds_per_day(3))
print(seconds_per_day())

def area_of_circle(radius):
    return 3.14*radius**2


def area_of_disc(outer, inner):
    return area_of_circle(outer)-area_of_circle(inner)


print(area_of_disc(10, 3))

x = 10
def fn(x):
    print(x)
    x = 20
    print(x)

print(x)
fn(0)
print(x)