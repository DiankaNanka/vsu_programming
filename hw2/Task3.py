print('Введите длину треугольника: ')
N = int(input('N: '))
for i in range(N):
    print('*' * (i + 1) + '*' * (i - N))
