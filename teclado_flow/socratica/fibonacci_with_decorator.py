from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 1:
        raise ValueError('n must be a positive int')


    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1)+fibonacci(n-2)

# for i in range(1, 501):
#     print(i, ':', fibonacci(i))

print(fibonacci(-2))