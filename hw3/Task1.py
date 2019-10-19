d = {'+','-','/','*','%'}
i = input('Введите пример: ')
s = set(i)
for x in ['**','//']:
    if x in i:
        sumb = x
        break
else:
    sumb = list(d & s)[0]
index = i.find(sumb)

a = int(i[:index])
b = int(i[index + len(sumb):])
d = {'+': a + b,
     '-': a - b,
     '/': a / b,
     '*': a * b,
     '%': a % b,
     '//': a // b,
     '**': a ** b}
print(d[sumb])