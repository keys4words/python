#[1, 2, 3] --> [2, 4, 6]
def double_array(arr):
    return [2*i for i in arr]

arr1 = [1, 2, 3]
print(arr1)
print(double_array(arr1))
print('='*18)


def return_square_array(arr):
    return sum([i**2 for i in arr])

print('sum =', return_square_array(arr1))
print('='*18)

def drink_volume(time):
    return int(time/2)

print(drink_volume(3))
print(drink_volume(6.7))
print(drink_volume(11.8))
print('='*18)

def transform_string_with_space(s):
    return s.upper() if s.find(' ')!= -1 else s.lower()

print(transform_string_with_space('Hello World!'))
