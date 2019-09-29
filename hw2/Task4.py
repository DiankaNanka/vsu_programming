print('Введите пример: ')
a = str(input())
if a.count('(') > a.count(')'):
    b = a.count("(") - a.count(")")
    print('Не хватает закрывающих скобок: ')
    print(b)
else:
    b = a.count(")") - a.count("(")
    print('Не хватает открывающих скобок: ')
    print(b)
