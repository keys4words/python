# recursion as analog of infinite loop
# def question(message):
#     if input(message + ': ').lower() == 'always':
#         return
#     else:
#         print('Think carefully...')
#     question(message)
#
#
# question('Your motto?')
# print('Nice!!!')

#Evklid algorytm
# def evklid(a, b):
#     if b == 0:
#         return a
#     return evklid(b, a%b)
#
# print(evklid(102, 68))

#recursion - problems
def factorial1(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def factorial2(n):
    if n==0:
        return 1
    return n*factorial2(n-1)

from timeit import Timer
import sys

# t1 = Timer('factorial1(10000)', 'from __main__ import factorial1')
# print('factorial one', t1.timeit(number=1), 'milliseconds')
# sys.setrecursionlimit(10000)
# print('recursion limits =', sys.getrecursionlimit())
# t1 = Timer('factorial2(9000)', 'from __main__ import factorial2')
# print('factorial two', t1.timeit(number=1), 'milliseconds')

# def factorial3(n, acc = 1):
#     if n <= 1:
#         return acc
#     return factorial3(n-1, n*acc)

# t1 = Timer('factorial3(1000)', 'from __main__ import factorial3')
# print('factorial three', t1.timeit(number=1), 'milliseconds')

def power1(base, exp):
    res = 1
    for i in range(exp):
        res *= base
    return res

def power2(base, exp):
    if exp == 0:
        return 1
    return base * power2(base, exp-1)

def power3(base, exp):
    if exp == 0:
        return 1
    if exp%2 == 0:
        return power3(base, exp/1)**2
    return base * power3(base, exp-1)

t1 = Timer('power1(2, 1000)', 'from __main__ import power1')
print('power one', t1.timeit(number=1), 'milliseconds')
t2 = Timer('power2(2, 10)', 'from __main__ import power2')
print('power two', t2.timeit(number=1), 'milliseconds')
# t3 = Timer('power3(2, 2)', 'from __main__ import power3')
# print('power three', t3.timeit(number=1), 'milliseconds')

#O(2**n)
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)

#O(n) + memory fo list!
def fib_list(n):
    f = [0, 1, 1]
    for i in range(3, n):
        f.append(f[i-1] + f[i-2])
    return f[len(f)-1]

# O(n)
def fib(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a
