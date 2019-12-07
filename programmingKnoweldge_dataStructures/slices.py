a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
c = '0123456789'

x = slice(0,7, 2)
print(a[x])
print(b[4:])
print(c[:])
print(c[::3])
print('python'[-2])
print(a[::-1])
print(a[:-3:-1])
print(a[-3::-1])
