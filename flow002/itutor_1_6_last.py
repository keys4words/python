n=[int(i) for i in input().split(' ')]
for i in range(len(n)):
    j=i
    while j>0 and n[j-1]>n[j]:
        n[j], n[j-1]=n[j-1], n[j]
        j-=1

print(*n)