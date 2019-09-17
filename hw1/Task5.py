print('Введите значения точки X и Y:')
X = int(input('X: '))
Y = int(input('Y: '))
if X > 0 and Y > 0:
    print('1 четверть')
elif X > 0 and Y < 0:
    print('4 четверть')
elif X < 0 and Y > 0:
    print('2 четверть')
elif X < 0 and Y < 0:
    print('3 четверть')
else:
    print ('лежит на оси')
    
