n = int(input())
s = str(n) + ' программист'
if 0<=n<=1000:
    if n == 0 or n%10 == 0:
        s += 'ов'
    # elif n//10 == 1:




print(s)