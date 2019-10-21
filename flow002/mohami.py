numbers=[4, 6, 7, 8, 4]
# numbers.remove(999)
print(numbers.index(7))
print(6 in numbers)
print(numbers.count(4))
numbers.sort()
numbers.reverse()
print(numbers)
numbers2=numbers.copy()
numbers2[0]=1000
print(numbers)

print('=============')
numbers=[2, 5, 6, 2, 9, 0, 2]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

print('=============')
numbers=(1, 3, 4)
x, y, z = numbers
print(y)

print('=============')
customer={
    'name':'John Doe',
    'age':30,
    'is_verified': True
}
print(customer.get('Age', 0))

print('=========')
# phone=input('Phone: ')
# digits_mapping={
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine'
# }
# s=''
# for ch in phone:
#     s+=(digits_mapping.get(ch, "!")+' ')
# print(s)

message=input('>')
words=message.split(' ')
emojis={
    ':)':'😀',
    ':(':'😢 '
}
out=''
for word in words:
    out+=emojis.get(word, word) + " "
print(out)