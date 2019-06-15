str = input()
res = []
while str!='end':
    line=[int(i) for i in str.split()]
    res.append(line)
    str = input()

print(res)