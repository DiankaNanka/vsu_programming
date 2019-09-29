print('Введите числа: ')
num = input()
list_num = []
while num:
   list_num.append(num)
   num = input()
list_num = (sorted((list_num), reverse = True))
print("".join(list_num))
