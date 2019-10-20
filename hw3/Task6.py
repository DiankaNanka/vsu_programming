from math import sqrt
sqrt = int
def num_a(f):
    for i in range(2, sqrt(f) + 1):
        if not f % i:
            return True
    return False

num = float(input('Введите число: '))
num_id = {True: 'простое', False: 'сложное'}
print(num_id[num_a(num)])
