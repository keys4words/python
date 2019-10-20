result = None
a = float(input('Number 1: '))
b = float(input('Number 2: '))

try:
    result = a / b
except ZeroDivisionError as e:
    print('ZeroDivisionError = ', type(e))
except TypeError as e:
    print('TypeError = ', e)

else:
    print('__else__')
finally:
    print('__finally__')

print(result)
print('End')