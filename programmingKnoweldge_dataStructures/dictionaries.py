D = {'name': 'max', 'age': 43, 'years': 2004}
print(D['age'])
E = {'name': 'Tom', 15: 44, 15.1: 34.55, True: False, (2,4): 5}
print(E[True])
print(E[(2, 4)])
print(E[15.1])
print(len(E))
print(D.get('name1'))
# print(D['name1'])
D['surname'] = 'Zhar'
print(D)
D.pop('surname')
print(D)
E.clear()
print(E)
del E
# print(E)
D.update({'name': 'Maximus'})
print(D)
# print(D.keys())
# print(D.values())
# print(D.items())
D.popitem()
print(D)
