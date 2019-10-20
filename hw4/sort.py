def insertion_sort(nums):
    # Создаем копию входящей структуры (она может быть не только списком)
    list_nums = list(nums)
    # Граница такая, т.к. будет идти сравнение [i] и [i+1], исключаем выход за список
    for i in range(len(list_nums) - 1):
        # Нужен итератор, который пойдет в обратном порядке
        j = i
        while j >= 0 and list_nums[j + 1] < list_nums[j]:
            # Меняем местами переменные
            list_nums[j + 1], list_nums[j] = list_nums[j], list_nums[j + 1]
            # Шаг назад
            j -= 1
    return(list_nums)
nums = input()
print(insertion_sort(nums))
