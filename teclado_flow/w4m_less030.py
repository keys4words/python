# from os import *
# from random import randint, shuffle
#
#
# print(os.getcwd())
# print(randint(1, 100))
# l = [1, 3, 4, 5, 6]
# shuffle(l)
# print(l)

import libs

f = libs.get_count
f1 = libs.get_len

# print(libs.get_count('hello', 'l'))
# print(libs.get_len('hello'))

print(f('hello', 'l'))
print(f1('hello'))