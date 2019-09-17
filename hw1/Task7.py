print('Введите значения отрезков x и y: ')
x = int(input('x: '))
y = int(input('y: '))
b = 0
for n in range(x, y + 1):
    if not n % 5:
        b += n
print(b)
