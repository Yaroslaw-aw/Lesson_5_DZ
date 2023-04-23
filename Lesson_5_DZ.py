import random

# Задача 1. Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

def task1():
    n = random.randint(7, 20)
    nums = [random.randint(1, 10) for _ in range(n)]
    print(nums)
    nums = list(filter(lambda x: x > 5, nums))
    print(nums)

# Задача 2. Дан список случайных чисел.
# Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

def task2():
    n = random.randint(3, 10)
    numbers = [random.randint(1, 10) for _ in range(n)]
    print(numbers)
    length = len(numbers)     
    j = 0
    while j < length:
        result = []  
        min = numbers[j]
        result.append(min)
        i = j + 1
        flag1 = True
        while flag1:
            if result[len(result)-1] < min:
                result.append(min)
            if i == length:
                flag1 = False
                continue
            flag = True
            while flag:
                if min < numbers[i]:
                    min = numbers[i]
                    i += 1
                    flag = False
                else:
                    i += 1
                    flag = False
        if len(result) > 1:
            print(result)
        j += 1
task2()




# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте,
# сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. Список уникальных элементов [1, 4, 2, 3, 6, 7]


def array():
    nums = [random.randint(0, 10) for _ in range(10)]
    print(nums)    
    unique = list(set(nums))
    repeat_sum = 0
    len_unique = len(unique)   
    for i in range(len_unique):
        repeat = 0
        repeat = nums.count(unique[i]) 
        if repeat > 1:
            repeat_sum += repeat    
        print(f'{unique[i]} - {repeat}')     
    print(f'{repeat_sum} элементов совпадают')
    print(f'Список уникальных элементов: ', unique)

