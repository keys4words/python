# no_of_ipv6 = 2**128
# print(no_of_ipv6)
# no_of_digits = len(str(no_of_ipv6))
# print(no_of_digits)
# phone = {'brand': '3LAB', 'price': 650.2, 'seller': 'mbg ltd'}
# phone['q-ty']=1000
# phone.update({'os': 'android'})
# print(phone)
phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
price = phone['Price']
vat = format(price*0.19, '.2f')
print(float(vat))

lst =[1, 2.3, 'abc', (5, 6, 'x', 'y')]
my_var = str(lst[1])+lst[2][0]+lst[-1][-1]
print(my_var)

languages = ['English', 'Python', 'Java', 'Golang', 'German']
print(languages[1:-1])

phone1 = ['1111', '2222', '2222', '1111']
phone2 = ['1111', '3333', '3333', '1111']
unite = set(phone1) | set(phone2)
print(unite)

my_str  = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
lst = my_str.split()
interface_max = lst[0]+'!'+lst[-1]
print(interface_max)