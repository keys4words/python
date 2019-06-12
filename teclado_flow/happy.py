n = input()
sum1, sum2 = 0, 0
for i in range(6):
    if i < 3:
        sum1 += int(n[i])
    else:
        sum2 += int(n[i])
res = 'Счастливый' if sum1 == sum2 else 'Обычный'
print(res)