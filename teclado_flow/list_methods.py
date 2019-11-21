l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
# l[:2] = ['Maximus', 'wins']
l.append('new')
names = ['Ivanov', 'Petrov', 'Sidorov']
l.extend(names)
l2 = ['hey', 'hello']
l += l2
l.insert(4, False)
l.remove('hello')
print(l.pop(2))
print(l.count('new'))

l3 = ['hello', 'hi', 'max', 'knew', 'oath']
l3.sort(reverse=True)
print(l3)

print(l)
# print(names[5])