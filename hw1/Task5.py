print('Введите значения точки X и Y:')
X=int(input('X: '))
Y=int(input('Y: '))
if X!=0 and Y!=0:
    if X*Y > 0:
        if X > 0:
            print('1 четверть')
        else:
            print('3 четверть')
    else:
        if X > 0:
            print('4 четверть')
        else:
            print('2 четверть')
else:
    print ('лежит на оси')
    
