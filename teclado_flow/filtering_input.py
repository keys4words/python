in_arr = [int(i) for i in input().split()]
filt = int(input())
filt_arr = []
for i in range(len(in_arr)):
    if in_arr[i]==filt:
        filt_arr.append(i)
if len(filt_arr)==0:
    print('Отсутствует')
else:
    print(*filt_arr)

print('============')
i=0
while in_arr.count(filt)!=0 and i<len(in_arr):
    print(in_arr.index(filt, i), end=' ')
    i+=1
else:
    print('Отсутствует')