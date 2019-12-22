def palindrom_one(string):
    reverse = ''
    i = len(string)-1
    while i >= 0:
        reverse += string[i]
        i -= 1
    if string.lower() == reverse.lower():
        return True
    return False

def palindrom_two(string):
    mid = len(string)//2
    j = len(string)-1
    for i in range(mid):
        if string[i] != string[j]:
            return False
        j -= 1
    return True

def palindrom_three(string):
    s1 = list(string)
    s2 = s1.copy()
    s2.reverse()
    if s1 == s2:
        return True
    return False

def sum_one(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sum_two(n):
    sum = (n*(n+1))/2
    return sum

from timeit import Timer
# t = Timer('sum_one(10000)', 'from __main__ import sum_one')
# print('{0:.6f}'.format(t.timeit(number=1)))
#
# t = Timer('sum_one(100000)', 'from __main__ import sum_one')
# print('{0:.6f}'.format(t.timeit(number=1)))
#
# t = Timer('sum_one(1000000)', 'from __main__ import sum_one')
# print('{0:.6f}'.format(t.timeit(number=1)))

t = Timer('sum_two(10000)', 'from __main__ import sum_two')
print('{0:.6f}'.format(t.timeit(number=1)))

t = Timer('sum_two(100000)', 'from __main__ import sum_two')
print('{0:.6f}'.format(t.timeit(number=1)))

t = Timer('sum_two(1000000)', 'from __main__ import sum_two')
print('{0:.6f}'.format(t.timeit(number=1)))

print('*'*15)
def anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    array = list(s2)
    pos1 = 0
    success = True
    found = False
    while pos1 < len(s1) and success:
        pos2 = 0
        found = False
        while pos2 < len(array) and not found:
            if s1[pos1] == array[pos2]:
                found = True
            else:
                pos2 += 1
            if found:
                array[pos2] = None
            else:
                success = False
            pos1 += 1
    return success

def anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    array1 = list(s1)
    array2 = list(s2)
    array1.sort()
    array2.sort()

    pos = 0
    length = len(s1)
    while pos < length:
        if array1[pos] != array2[pos]:
            return False
        pos += 1
    return True


def anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    array1 = list(s1)
    array2 = list(s2)
    array1.sort()
    array2.sort()

    if array1 == array2:
        return True
    return False

def anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    array1 = [x for x in range(26)]
    array2 = [x for x in range(26)]

    a_pos = 97
    for char in s1:
        pos = ord(char) - a_pos
        array1[pos] = (array1[pos] or 0) + 1
    for char in s2:
        pos = ord(char) - a_pos
        array2[pos] = (array2[pos] or 0) + 1

    for i in array1:
        if array1[i] != array2[i]:
            return False
    return True