print(1)
# x = 'a' * 'b'

try:
    age = input('Input something:  ')
    age = int(age)
    if age < 18:
        raise Exception('Age must be more 18 years')
    print("You may in")
    # long = 20
    # short = 2
    # total = long * 3 + 'short' * 2
    # x = 'a' > 1
    # print(long/0)
    # print(total)
except EOFError:
    print('ВЫ сделали мне EOF ')
except ValueError as e:
    print(e)
except (NameError, TypeError) as e:
    if type(e) == TypeError:
        print('My TypeError message')
    print('Oops!')
except KeyboardInterrupt:
    print('Вы отменили операцию!')
# except TypeError:
#     print('Type error')
# except:
#     print('General error')

# else:
#     print('else message' , txt)

except Exception as e:
    print(e)
finally:
    print('Finally message')

print('The end')
