print('Введите значения точки X и Y:')
x = float(input('X: '))
y = float(input('Y: '))
if x > 0 and y > 0:
    print('1 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
else:
    print ('лежит на оси')
