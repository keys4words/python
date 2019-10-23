def outerFunction(text):
    def innerFunction():
        print(text)
    return innerFunction

a = outerFunction('Max')
del outerFunction
a()


def pop(list):
    def get_last_item(my_list):
        return my_list[len(list) - 1]
    list.remove(get_last_item(list))
    return list

a = [1, 2, 3, 4, 5]
print(pop(a))
print(pop(a))
print(pop(a))
print(pop(a))

def nth_power(exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of

square = nth_power(2)
print(square(5))
cube = nth_power(3)
print(cube(3))