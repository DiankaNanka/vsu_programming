a = input('Введите числа: ')
list_a = []
list_b = []
while a:
    list_a.append(a)
    a = input()
list_b = set(list_a)
for i in list_b:
    print(i, list_a.count(i))    
