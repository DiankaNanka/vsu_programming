a = input('Введите пример: ')
count_ob = a.count('(')
count_cb = a.count(')')

if count_ob > count_cb:
    print('Не хватает закрывающих скобок: ', count_ob - count_cb)
else:
    print('Не хватает открывающих скобок: ', count_cb - count_ob)
