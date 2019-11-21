t1 = (1, 2, 3)
l1 = [1, 2, 3]
#
# print(t1, type(t1))
# print(l1, type(l1))

# t2 = 1, 2, 3
# print(type(t2))

# t3 = tuple([1, 2, 3])
# print(type(t3))

# t4 = (1,)
# print(type(t4))
#
# t5 = tuple('something')
# print(t5, t5[4])
#
# print('*'*18)
# print('tuple =', t1.__sizeof__() )
# print('list =', l1.__sizeof__() )
#
# print('*'*18)
# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(len(t3))
#
# print('*'*18)
# print(t3.count('x'))
# sym = 'x'
# if sym in t3:
#     print(t3.index(sym))
# else:
#     print('no')
#
# print('*'*18)
# for sym in t3:
#     if sym == ' ':
#         continue
#     print(f'"{sym}"', end=' ')

# t1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t1, id(t1))
# t1[2][0] = 'new'
# print(t1, id(t1))

t1 = (1, 2, 3)
x, y, z = t1
print(x, y, z)
print('*'*18)


x = 1
y = 2
print(x, y)
x, y = y, x
print(x, y)
