# s1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(s1, type(s1))
#
# s2 = set('hello')
# print(s2)
#
# s3 = {i for i in range(1, 11)}
# print(s3, type(s3))
#
# s4 = {5, 3, 10, 1, 555}
# print(s4)
#
# s5 = {}
# print(type(s5))
#
# s6 = set()
# print(type(s6))
#
# nums = [1, 2, 4, 2, 1, 1, 5]
# nums2 = list(set(nums))
# print(nums2)

# a = set('abracadabra')
# b = set('alacazam')
# print(a, b, sep='\n')
#
# c = a - b
# print('a-b', c)
# d = a | b
# print('a | b', d)
# e = a & b
# print('a & b', e)
# f = a ^ b
# print('a ^ b', f)

# s1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = s1.copy()
# print(s2, id(s1), id(s2))
# s1.add('melon')
# print(s1)
# s1.discard('apple2')
# if 'apple' in s1:
#     print('OK')
#
# s1.clear()
# print(s1)

a = frozenset('hello')
print(a)
print(a.add('test'))