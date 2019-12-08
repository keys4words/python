import random

n1 = random.randrange(1, 11)
n2 = random.randrange(1, 11)

answer = input(f'Сколько будет {n1} + {n2}? ')
test = answer.replace('.', '', 1)

if not test.isdigit():
    print('Надо ввести число!')
else:
    if answer == test:
        answer = int(answer)
    else:
        answer = float(answer)

    if answer == n1+n2:
        print('Правильно')
    else:
        print('Не верно!')
