d = {'a': 100, 'b': 200, 'c': 300}
print(d['b'])
d['a'] = 900
print(d)
# print(d['h'])

print('y' in d)
print(d.get('h', None))

hello = {
    'ru': 'Добрый день',
    'en': 'Good day',
    'de': 'Guten tag',
    'dk': 'God dag',
    'default': 'Unknown language'
}

s = input('Введите код: ')
greet = hello.get(s, hello['default'])
print(greet)
