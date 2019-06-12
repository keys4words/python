a,b=int(input()), int(input())
s=count=0
for i in range(a, b+1):
    if i%3==0:
        s+=i
        count+=1
print(s/count)