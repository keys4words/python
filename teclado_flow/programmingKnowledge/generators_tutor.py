def my_func():
    # n = 1
    for i in range(5):
        print('-------------------', i)
        yield i
    # n += 1
    # yield n
    # print('-------------------', n)
    # n += 1
    # yield n
    # print('-------------------', n)
    # n += 1
    # yield n
    # print('-------------------', n)
    # n += 1

x = my_func()

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


def list_iterator(lst):
    for i in lst:
        yield i


a = [1, 9, 13, 5, 6]
my_list = list_iterator(a)

print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))

for x in my_list:
    print(x)