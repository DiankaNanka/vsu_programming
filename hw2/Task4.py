def brackets(a):
    count_ob = a.count('(')
    count_cb = a.count(')')
    if count_ob > count_cb:
        return('Не хватает закрывающих скобок: ', count_ob - count_cb)
    elif count_ob < count_cb:
        return('Не хватает открывающих скобок: ', count_cb - count_ob)
    return('Всех скобок хватает!')
        
print(brackets(input('Введите пример: ')))

