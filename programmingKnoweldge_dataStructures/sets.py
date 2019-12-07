# A = {1, 12, 6, 2, 8, 12}
# print(A)
# print(len(A))
# A.add(44)
# A.add(44)
# print(A)
# A.update([45, 67, 88])
# print(A)
# A.remove(45)
# print(A)
# A.discard(120)
# print(A)
# A.pop()
# print(A)
# name = {'max', 'tom', 'den'}
# name.clear()
# print(name)
# del name
#
# name = set({'max', 'tom', 'den'})
# print(name)
z = set([1, 3, 4])
print(z, type(z))
A = {2, 4, 5, 7, 9, 10, 14, 15}
B = {10, 11, 12, 13, 14, 16, 18}
# print(A | B)
print(A.union(B))
# print(A.intersection(B))
print(A & B)
print(A - B)
print(B-A)
# print(A.symmetric_difference(B))
print(A ^ B)
print(B ^ A)

# print(A[0])
