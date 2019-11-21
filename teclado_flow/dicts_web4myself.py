# d = {}
# print(d, type(d))
#
# d1 = {'title': 'Sony',
#       'price': 100}
# print(d1['title'])
#
# d2 = dict(title='iPhone', price=1341)
# print(d2)

# users = [
#     ['bob@mail.ru', 'Bob Marley'],
#     ['kaili@ya.ru', 'Kayli Minogue'],
#     ['john_doe@gmail.com', 'John Doe']
# ]
#
# print(users)
# d_users = dict(users)
# print(d_users)

# products = dict.fromkeys(['price1', 'price2', 'price3', 'price4'])
# print(products, type(products))

# nums = {i: i**2 for i in range(1, 10)}
# print(nums)

d1 = {'title': 'Sony',
      'price': 100}
d2 = dict(title='iPhone', price=1341)
print(d1, d2)
print(d1['title'], d2.get('price2', 'n/a'))

for key,value in d1.items():
    print(f'{key} -> {value}')

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 345},
    {'title': 'LG', 'price': 546}
]

print('='*15)
for product in products:
    print(product['title'], product['price'])

print('='*15)
print(d1.items())
# print(d1.keys())
# print(d1.pop('title', 'No'))
# print(d1)
# print(d1.popitem())

print(d1.setdefault('title2', 111))
print(d1)
d1.update({'test': 'value'})
print(d1)
print(d1.values())





