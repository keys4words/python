import random
num = random.randrange(1, 11)

while True:
    answer = input('Введите число: ')
    if not answer.isdigit():
        print('Надо ввести число')
        continue
    else:
        answer = int(answer)
        if answer > num:
            print('Перелет')
        elif answer < num:
            print('Недолет')
        else:
            print('Correct!')
            break


