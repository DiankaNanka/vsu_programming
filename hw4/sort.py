def insertion_sort(nums):
    # Преобразуем к типу список входящую структуру
    list_nums = list(nums)
    # Граница такая, т.к. будет идти сравнение [j] и [j - 1], исключаем выход за список
    for i in range(1, len(list_nums)):
        # Нужен итератор, который пойдет в обратном порядке
        j = i
        while j and list_nums[j - 1] > list_nums[j]:
            # Меняем местами переменные
            list_nums[j - 1], list_nums[j] = list_nums[j], list_nums[j - 1]
            # Шаг назад
            j -= 1
    return list_nums


nums = input()
print(insertion_sort(nums))
