print('Введите длину треугольника: ')
N = int(input('N: '))
i = int(1)
for i in range(N):
    print('*' * (i + 1) + '*' * (i - N))
