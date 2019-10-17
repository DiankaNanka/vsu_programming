d = {'+', '-', '/', '*', '//', '%', '**'}
i = input('Введите пример: ')
s = set(i)
for x in ['**', '//']:
    if i.find(x) != -1:
        index = i.find(x)
        sumb = x
        break
else:
    sumb = list(d & s)[0]
    index = i.find(sumb)

a = int(i[:index])
b = int(i[index + len(sumb):])
d = {sumb == '+': a + b,
     sumb == '-': a - b,
     sumb == '/': a / b,
     sumb == '*': a * b,
     sumb == '//': a // b,
     sumb == '%': a % b,
     sumb == '**': a ** b}
print(d[True])
