# def get_square(num):
#     return num ** 2
#
# print(get_square(5))


sq = lambda num: num ** 2
print(sq(10))

print((lambda x: x*34)(10))

l = [1, 2, 3]
def get_double(l):
    # return [i * 2 for i in l]
    return list(map(lambda x: x ** 2, l))

print(get_double(l))
