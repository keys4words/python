# i = 0
# while i<5:
#     a,b=input().split()
#     a = int(a)
#     b = int(b)
#     if a==0 and b==0:
#         break
#     if a==0 or b==0:
#         continue
#     print(a*b)
#     i+=1

i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i)