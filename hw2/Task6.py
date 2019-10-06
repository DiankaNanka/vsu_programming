ln = input('Введите строку: ')
ln2 = ''
for i in ln:
    if '0' <= i <= '9':
        ln2 += i
n = int(input('Введите номер: '))
print (ln2[n])

    
