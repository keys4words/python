import random

x = random.randint(1, 100)
user_num = 0
cnt = 0
while True:
    user_num = int(input('Я загадал число от 1 до 100. Угадай его: '))
    cnt += 1
    if user_num == x:
        print(f'Ты угадал число за {cnt} попыток')
        print('Поздравляю!')
        if input('Сыграем еще? y/n  ') == 'y':
            x = random.randint(1,100)
            cnt = 0
        else:
            print('Спасибо за игру!')
            break
    elif user_num > x:
        print('Перелет')
    else:
        print('Недолет')
