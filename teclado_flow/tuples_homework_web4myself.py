def separate_polyndroms(arr):
    return [word for word in arr if word.lower().replace(' ', '') == word[::-1].lower().replace(' ', '')]

print(separate_polyndroms(['мадам', 'топот', 'test', 'madam', 'word']))
print(separate_polyndroms(['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']))

dots = '..'
l = list(range(1, 10))
l2 = list('hello')
print(l, l2)
my_str = dots.join(map(str, l))
my_str2 = dots.join(l2)
print(my_str)
print(my_str2)


