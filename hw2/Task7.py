from random import randint
rd = randint(0, 100)
introduce = int(input('Введите загаданное число: '))
while rd != introduce:
    if introduce > rd:
        print('Загаданное число меньше!')
        introduce = int(input('Введите загаданное число: '))
    else:
        print('Загаданное число больше!')
        introduce = int(input('Введите загаданное число: '))
print('Вы угадали число!')
