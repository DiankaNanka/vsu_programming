print('Введите строку: ')
line = input('line: ')
if line == line[::-1]:
    print('Это палиндром')
else:
    print('Это не палиндром')
