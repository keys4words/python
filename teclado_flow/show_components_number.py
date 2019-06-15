n=int(input())
res=[]
for i in range(1, n+1):
    res +=[i]*i
    if len(res)>=n:
        break

print(*res[:n])