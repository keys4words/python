n = 1
while n <= 100:
    n = int(input())
    if n < 10:
        continue
    if n>100:
        break
    else:
        print(n)
