name = 'John'
age = 30
title = 'Philips'
price = 444
# print('My name is %(name)s. I\'m %(age)d' %{'name': name, 'age':age})
# print('My name is %s. I\'m %d' %(name, age))
# print('Title: %s, price: %.2f' %('Sony', 40))
# print('Title: {1}, price: {0}'.format('Sony', 40))
# print('Title: {title}, price: {price}'.format(title=title, price=price))
print(f'Title: {title}, price: {price/100}')

x = 0
res = 'OK' if x else 'NO'
print(res)

print([i for i in 'hello' if i not in 'aeuyo'])