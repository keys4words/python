a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range(a, b+1):
    if i%2==1:
        s += i
print(s)
print('==============')
a, b = (int(i) for i in input().split())
if a%2==0:
    a+=1
s=0
for i in range(a, b+1, 2):
    s+=i
print(s)