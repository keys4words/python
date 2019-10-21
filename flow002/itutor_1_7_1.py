n=[int(i) for i in input().split(' ')]
c={}
for el in n:
    c[el]=n.count(el)

res=[i for i in c.keys() if c[i]>1]
res.sort()
print(*res)