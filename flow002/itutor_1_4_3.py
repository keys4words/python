n=int(input())

def ret_binary(n:int):
    s=''
    while n//2>=1:
       s+=str(n%2)
       n=n//2
    s+=str(n%2)
    return s[::-1]

print(ret_binary(n))
print(bin(n))