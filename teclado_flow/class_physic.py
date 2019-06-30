n=int(input())
l=[int(i) for i in input().split(' ')]
l.append(n)
l.sort(reverse=True)
print(l.index(n)+l.count(n))
