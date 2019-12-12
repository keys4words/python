name = 'Popandopulo'
if name.startswith('Pop'):
    print('yes')
if 'a' in name:
    print('string consists \'a\'')
if name.find('dop') != -1:
    print('string has substring "dop"')
delimeter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimeter.join(mylist))