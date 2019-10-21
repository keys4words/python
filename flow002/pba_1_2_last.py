objects = [1, 2, 1, 2, 3]
ans = 0
res=set()
for obj in objects: # доступная переменная objects
    res.add(obj)

ans=len(res)
print(ans)