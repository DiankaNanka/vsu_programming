print('Введите число: ')
N = float(input('N: '))
if N == int(N) or not N % 1:
    print('Число не дробное')
else:
    print('Число дробное')
