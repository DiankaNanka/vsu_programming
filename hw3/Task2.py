def s(season):
    return({3 <= season <= 5 : 'Весна',
     6 <= season <= 8 : 'Лето',
     9 <= season <= 11 : 'Осень',
     1 <= season <= 2 or season == 12 : 'Зима'}[True])
season = int(input('Введите число: '))
print(s(season))
