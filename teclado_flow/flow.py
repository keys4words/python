# def hundred_numbers():
#     i = 0
#     while i < 100:
#         yield i
#         i += 1
# g = hundred_numbers()
# print(next(g), end=' ')
# print(next(g), end=' ')
# print(next(g), end=' ')
# print(next(g))
# print(list(g))
#
# print([x * 2 for x in hundred_numbers()])

a = int(input())
b = int(input())
i = a
s = 0
while i <= b:
    s += i
    i += 1

print(s)