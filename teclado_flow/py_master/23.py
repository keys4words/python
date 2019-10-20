def myfunc(num):
    res = int(num) + int(num*2) + int(num*3)
    return res

print(myfunc('5'))

mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']
unique_mac = list(set(mac))
print(unique_mac)
unique_mac2=list()
for el in mac:
    if el not in unique_mac2:
        unique_mac2.append(el)
print(unique_mac2)