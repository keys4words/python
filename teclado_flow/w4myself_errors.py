# print('hello')
#
# try:
#     num = 100/4
# except ZeroDivisionError:
#     print("Division by 0")
#     num = 0
# except TypeError:
#     num = 1
# except Exception:
#     num = 2
# else:
#     print('Else')
# finally:
#     print('Finally')
#
# print(num)

while True:
    try:
        num = int(input("Enter your number: "))
        print(f'100 / {num} = {100/num}')
        break
    except ZeroDivisionError:
        print('Number must be greater than zero!!!')
    except ValueError:
        print('Number must be a number')
